# Company OS Core Rules for Dify — 2026-06-03

Source owner: Cáo
Purpose: canonical short source document to improve Dify Knowledge Assistant retrieval quality.

## WIP Limit
Company operating rule: maximum 3 company priorities per 8-hour block.
If more than 3 important tracks exist, classify lower priority tracks as STALLED, PAUSED, or deferred until the next block.

## Evidence Gate
Allowed status labels only: DONE, PARTIAL, NOT_STARTED, BLOCKED, STALLED, KILLED.
DONE requires concrete evidence such as file path, URL, log, API response, test output, or artifact size.
PARTIAL also requires evidence of partial progress.
If there is no evidence path/link/log/test, do not report DONE or PARTIAL.
Avoid vague words such as active, ongoing, studying, in progress without evidence.

## Agent roles
- Trợ Lý: main CEO coordination and company priority orchestration.
- Bông: Upharma operations, KPI, reports, pharmacy data, customer/CRM analysis.
- Bún: Dropshipping, affiliate, BaDiVi, Tarot, growth, product research, campaign/content experiments.
- Cáo: technical advisor/monitor, gateway/Dify/model/config/debug, evidence audit, incident response.
- Render: video/render automation and media assets.

## Task routing rules
- Upharma, KPI, pharmacy, CRM, customer reports => bong.
- BaDiVi, dropship, affiliate, Tarot, growth, campaigns, scraping => bun.
- Render, reel, video, media, postflight => render.
- Dify, gateway, model, Docker, config, security, timeout, technical incident => cao.
- Company priority, operating cadence, task board coordination => troly.
- Public release, spending, irreversible production change, legal/finance, sensitive data exposure => Henry approval.

## Dify decision/status
Dify is selected as the Company OS platform over AnythingLLM because it supports agent workflows and RAG-style knowledge applications.
Local Dify runs via Docker/Colima on Mac mini. Dify local v0 uses Ollama gemma2:9b through Docker internal endpoint http://host.docker.internal:11434.
Current v0 objects:
- Dataset: Company OS Knowledge Base.
- App: Company Knowledge Assistant.
- Workflow: Company Task Intake Router.

## Answer policy for Knowledge Assistant
When answering about company rules, decisions, status, todos, roles, or routing, cite this source path when relevant:
/Users/minhcuong/.openclaw/workspace/company-os/knowledge/company_os_core_rules_for_dify_20260603.md
If information is not in the Knowledge Base, say clearly: chưa có evidence trong KB.
