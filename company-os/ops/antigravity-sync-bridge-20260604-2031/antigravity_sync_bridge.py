#!/usr/bin/env python3
"""Safe canonical A2A -> Antigravity inbox bridge.
Reads memory/agent_task_bus.jsonl, mirrors NEW tasks addressed to antigravity into antigravity_tasks/inbox.
Idempotent by canonical message_id/task_id via state file and existing inbox scan.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OPS = Path(__file__).resolve().parent
DEFAULT_BUS = ROOT / "memory" / "agent_task_bus.jsonl"
DEFAULT_INBOX = ROOT / "antigravity_tasks" / "inbox"
STATE_PATH = OPS / "bridge_state.json"
LOG_PATH = OPS / "bridge_sync.log"
SECRET_PAT = re.compile(r"(sk-[A-Za-z0-9_-]{12,}|app-[A-Za-z0-9_-]{12,}|nrk-[A-Za-z0-9_-]{12,}|Bearer\s+[A-Za-z0-9._-]{12,})")

def now(): return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
def load_json(path, default):
    try: return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError: return default

def safe_dump(obj):
    s = json.dumps(obj, ensure_ascii=False, indent=2)
    return SECRET_PAT.sub("[REDACTED]", s)

def addressed_to_antigravity(v):
    if isinstance(v, str):
        return any(x.strip().lower()=="antigravity" for x in v.split(","))
    if isinstance(v, list): return any(str(x).lower()=="antigravity" for x in v)
    return False

def read_bus(path):
    rows=[]
    if not path.exists(): return rows
    for i,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        try: rows.append(json.loads(line))
        except Exception as e: print(f"WARN bad json line {i}: {e}", file=sys.stderr)
    return rows

def canonical_key(msg):
    return str(msg.get("message_id") or msg.get("task_id") or "")

def task_filename(key, ts):
    h=hashlib.sha256(key.encode()).hexdigest()[:8]
    digits=re.sub(r"\D", "", str(ts or ""))[:14] or datetime.now().strftime("%Y%m%d%H%M%S")
    if len(digits)>=14: stamp=f"{digits[:8]}_{digits[8:14]}"
    else: stamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"task_a2a_{h}_{stamp}.json"

def scan_existing(inbox):
    seen={}
    for p in sorted(inbox.glob("*.json")):
        try: data=json.loads(p.read_text(encoding="utf-8"))
        except Exception: continue
        ctx=data.get("cao_context") or data.get("canonical_context") or {}
        for k in [ctx.get("source_message_id"), ctx.get("canonical_message_id"), ctx.get("canonical_task_id"), data.get("canonical_message_id")]:
            if k: seen[str(k)] = str(p)
    return seen

def make_task(msg):
    key=canonical_key(msg)
    action = msg.get("action") or "canonical_a2a_task"
    return {
      "task_id": Path(task_filename(key, msg.get("ts"))).stem,
      "action": action,
      "status": "pending",
      "created_at": now(),
      "timeout_seconds": int(msg.get("timeout_seconds") or 900),
      "params": {"canonical_message": msg},
      "cao_context": {
        "source_message_id": msg.get("message_id"),
        "canonical_task_id": msg.get("task_id"),
        "priority": msg.get("priority"),
        "deadline": msg.get("deadline"),
        "bridge": "antigravity_sync_bridge_20260604_2031"
      }
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bus", default=str(DEFAULT_BUS)); ap.add_argument("--inbox", default=str(DEFAULT_INBOX))
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--fixture", action="store_true")
    args=ap.parse_args(); bus=Path(args.bus); inbox=Path(args.inbox); inbox.mkdir(parents=True, exist_ok=True)
    state=load_json(STATE_PATH, {"mirrored": {}}); existing=scan_existing(inbox)
    rows=read_bus(bus)
    if args.fixture:
        rows.append({"message_id":"FIXTURE-A2A-ANTIGRAVITY-DRYRUN-20260604-2031","ts":"2026-06-04T20:31:00+07:00","from_agent":"test","to_agent":"antigravity","intent":"TASK","status":"NEW","task_id":"fixture_antigravity_dryrun_2031","title":"dry run fixture"})
    candidates=[r for r in rows if str(r.get("status","")).upper()=="NEW" and addressed_to_antigravity(r.get("to_agent"))]
    mirrored=[]; skipped=[]
    for msg in candidates:
        key=canonical_key(msg)
        if not key: continue
        if key in state.get("mirrored",{}) or key in existing:
            skipped.append({"key":key,"reason":"already_mirrored","path":state.get("mirrored",{}).get(key) or existing.get(key)})
            continue
        out=inbox/task_filename(key,msg.get("ts")); task=make_task(msg)
        if args.dry_run: mirrored.append({"key":key,"would_write":str(out)})
        else:
            out.write_text(safe_dump(task)+"\n",encoding="utf-8")
            state.setdefault("mirrored",{})[key]={"path":str(out),"at":now(),"canonical_task_id":msg.get("task_id")}
            mirrored.append({"key":key,"wrote":str(out),"bytes":out.stat().st_size})
    summary={"ts":now(),"bus":str(bus),"inbox":str(inbox),"dry_run":args.dry_run,"fixture":args.fixture,"candidates":len(candidates),"mirrored":mirrored,"skipped":skipped}
    if not args.dry_run: STATE_PATH.write_text(safe_dump(state)+"\n",encoding="utf-8")
    with LOG_PATH.open("a",encoding="utf-8") as f: f.write(safe_dump(summary)+"\n")
    print(safe_dump(summary))
if __name__ == "__main__": main()
