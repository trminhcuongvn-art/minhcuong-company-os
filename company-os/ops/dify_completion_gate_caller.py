#!/usr/bin/env python3
"""
Dify Agent→Cáo Completion Gate caller.
Usage: python dify_completion_gate_caller.py --agent <name> --task-id <id> --status DONE --evidence <path> --rollback <text> --next <text>
"""
import argparse, json, urllib.request, os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = Path(__file__).parent / "dify_completion_gate_config.json"
config = json.loads(CONFIG_PATH.read_text())

def call_gate(agent, task_id, status, evidence, rollback, next_action):
    url = config["dify_base_url"].rstrip("/") + config["workflow_run_endpoint"]
    payload = {
        "inputs": {
            "agent_name": agent,
            "task_id": task_id,
            "status": status,
            "evidence": evidence or "",
            "rollback": rollback,
            "next_action": next_action
        },
        "response_mode": config.get("response_mode", "blocking"),
        "user": agent
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {config['completion_gate_api_key']}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        result = json.loads(r.read().decode())
    return result

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent", required=True)
    ap.add_argument("--task-id", required=True)
    ap.add_argument("--status", required=True, choices=["DONE","PARTIAL","BLOCKED","NOT_STARTED"])
    ap.add_argument("--evidence", default="")
    ap.add_argument("--rollback", required=True)
    ap.add_argument("--next", required=True, dest="next_action")
    args = ap.parse_args()
    result = call_gate(args.agent, args.task_id, args.status, args.evidence, args.rollback, args.next_action)
    print(json.dumps(result, ensure_ascii=False, indent=2))
