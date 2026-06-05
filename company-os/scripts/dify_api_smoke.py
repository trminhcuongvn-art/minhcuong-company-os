#!/usr/bin/env python3
import argparse, json, os, urllib.request

def post(url, key, payload):
    req=urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Authorization":"Bearer "+key,"Content-Type":"application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.status, json.loads(r.read().decode())

ap=argparse.ArgumentParser()
ap.add_argument('--base', default='http://localhost/v1')
ap.add_argument('--chat-key', default=os.getenv('DIFY_CHAT_KEY',''))
ap.add_argument('--workflow-key', default=os.getenv('DIFY_WORKFLOW_KEY',''))
args=ap.parse_args()
if args.chat_key:
    status,data=post(args.base+'/chat-messages', args.chat_key, {"inputs":{},"query":"API smoke: trả lời ok","response_mode":"blocking","conversation_id":"","user":"cao-smoke"})
    print('chat', status, data.get('answer'), data.get('conversation_id'))
if args.workflow_key:
    status,data=post(args.base+'/workflows/run', args.workflow_key, {"inputs":{"task":"API smoke task intake","requester":"cao","business_unit":"company-os","urgency":"normal","risk_notes":"internal"},"response_mode":"blocking","user":"cao-smoke"})
    print('workflow', status, data.get('data',{}).get('status'), data.get('workflow_run_id'))
