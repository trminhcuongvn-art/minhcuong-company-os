#!/usr/bin/env python3
import argparse,json,datetime,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
REG=ROOT/'company-os/ops/task_registry.jsonl'
BUS=ROOT/'memory/agent_task_bus.jsonl'
VALID={'DONE','PARTIAL','NOT_STARTED','BLOCKED','IN_PROGRESS'}
def now(): return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).isoformat()
def load():
 rows=[]
 if REG.exists():
  for l in REG.read_text(errors='ignore').splitlines():
   if l.strip(): rows.append(json.loads(l))
 return rows
def save(rows):
 REG.parent.mkdir(parents=True,exist_ok=True)
 REG.write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n',encoding='utf-8')
def add(args):
 rows=load(); tid=args.task_id or f"difytask_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
 r={"task_id":tid,"source":args.source,"owner":args.owner,"priority":args.priority,"status":"NOT_STARTED","risk_flags":{"cost_license":False,"production_data_write":False,"hard_to_rollback":False,"public_internal_data":False},"instruction":args.instruction,"required_evidence":["path","size_or_log","rollback"],"evidence":[],"blocker":None,"next":"ACK required","created_at":now(),"updated_at":now(),"sla_ack_minutes":args.sla_ack,"sla_done_minutes":args.sla_done}
 rows.append(r); save(rows); print(json.dumps(r,ensure_ascii=False,indent=2))
def dispatch(args):
 rows=load(); n=0
 BUS.parent.mkdir(parents=True,exist_ok=True)
 with BUS.open('a',encoding='utf-8') as f:
  for r in rows:
   if r['status']=='NOT_STARTED':
    msg={"message_id":f"DIFY-OPS-DISPATCH-{r['task_id']}","ts":now(),"from_agent":"dify_ops_cli","to_agent":r['owner'],"intent":"TASK","status":"NEW","priority":r['priority'],"task_id":r['task_id'],"title":"Dify Ops dispatch","instruction":r['instruction'],"required_evidence":r['required_evidence']}
    f.write(json.dumps(msg,ensure_ascii=False)+'\n'); r['status']='IN_PROGRESS'; r['updated_at']=now(); n+=1
 save(rows); print(json.dumps({"dispatched":n,"bus":str(BUS)},ensure_ascii=False))
def gate(args):
 st=args.status
 if st not in VALID: sys.exit('invalid status')
 ev=[]
 for p in args.evidence:
  q=Path(p)
  if not q.is_absolute(): q=ROOT/q
  if q.exists(): ev.append({"path":str(q),"bytes":q.stat().st_size})
 missing=[]
 if st in {'DONE','PARTIAL'} and not ev: missing.append('evidence_path')
 if st=='DONE' and args.blocker: missing.append('DONE_with_blocker')
 res={"status":"PASSED" if not missing else "REJECTED","claimed_status":st,"evidence":ev,"missing":missing,"blocker":args.blocker,"next":args.next,"checked_at":now()}
 out=ROOT/f"company-os/ops/evidence_gate_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
 out.write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({"result":res,"path":str(out)},ensure_ascii=False,indent=2))
def scan(args):
 rows=load(); changed=0; escal=[]; nowdt=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7)))
 for r in rows:
  try: upd=datetime.datetime.fromisoformat(r.get('updated_at') or r.get('created_at'))
  except Exception: upd=nowdt
  age=(nowdt-upd).total_seconds()/60
  if r.get('status')=='IN_PROGRESS' and age>=int(r.get('sla_ack_minutes',10)):
   r['status']='BLOCKED'; r['blocker']=f"No ACK after {int(age)}m SLA"; r['next']='Escalate to Cao / Dify Ops'; r['updated_at']=now(); changed+=1; escal.append(r['task_id'])
 save(rows)
 out=ROOT/f"company-os/ops/sla_scan_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
 out.write_text(json.dumps({'blocked':escal,'changed':changed,'checked_at':now()},ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({'changed':changed,'blocked':escal,'path':str(out)},ensure_ascii=False,indent=2))

def main():
 ap=argparse.ArgumentParser(); sub=ap.add_subparsers(required=True)
 a=sub.add_parser('add'); a.add_argument('--task-id'); a.add_argument('--owner',required=True); a.add_argument('--instruction',required=True); a.add_argument('--source',default='dify'); a.add_argument('--priority',default='P0'); a.add_argument('--sla-ack',type=int,default=10); a.add_argument('--sla-done',type=int,default=45); a.set_defaults(func=add)
 d=sub.add_parser('dispatch'); d.set_defaults(func=dispatch)
 g=sub.add_parser('gate'); g.add_argument('--status',required=True); g.add_argument('--evidence',action='append',default=[]); g.add_argument('--blocker'); g.add_argument('--next',default=''); g.set_defaults(func=gate)
 s2=sub.add_parser('scan'); s2.set_defaults(func=scan)
 args=ap.parse_args(); args.func(args)
if __name__=='__main__': main()
