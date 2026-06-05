#!/usr/bin/env python3
import importlib.util, json, time, sys
from pathlib import Path
ROOT=Path('/Users/minhcuong/.openclaw/workspace')
INBOX=ROOT/'antigravity_tasks/inbox'; LOG=ROOT/'company-os/ops/antigravity_watcher_daemon.log'
EXEC=ROOT/'antigravity_tasks/bin/antigravity_executor.py'
def log(m): LOG.open('a',encoding='utf-8').write(f'{time.strftime("%Y-%m-%dT%H:%M:%S%z")} {m}\n'); print(m)
spec=importlib.util.spec_from_file_location('ag_exec', EXEC); ag=importlib.util.module_from_spec(spec); spec.loader.exec_module(ag)
def run_once():
    before=set((ROOT/'antigravity_tasks/outbox').glob('*.json'))
    ag.run_watcher()
    after=set((ROOT/'antigravity_tasks/outbox').glob('*.json'))
    return len(after-before)
def loop(interval=1):
    INBOX.mkdir(parents=True,exist_ok=True); log('START watcher daemon')
    try:
      from watchdog.observers import Observer
      from watchdog.events import FileSystemEventHandler
      class H(FileSystemEventHandler):
        def on_created(self,e):
          if not e.is_directory and e.src_path.endswith('.json'):
            time.sleep(0.2); log(f'CREATED {e.src_path}'); run_once()
      obs=Observer(); obs.schedule(H(), str(INBOX), recursive=False); obs.start(); run_once()
      try:
        while True: time.sleep(3600)
      finally: obs.stop(); obs.join()
    except Exception as e:
      log(f'WATCHDOG_FALLBACK {e}')
      while True: run_once(); time.sleep(interval)
if __name__=='__main__':
    if '--once' in sys.argv: raise SystemExit(0 if run_once()>=0 else 1)
    loop()
