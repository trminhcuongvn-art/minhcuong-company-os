# Tool Registry

Status values: ADOPT / TRIAL / WATCH / REJECT
Phase values: NOW / PHASE_1 / PHASE_2 / LATER

| Tool | Status | Phase | Company use | Owner | Next action |
|---|---|---|---|---|---|
| Company OS task_board.jsonl | ADOPT | NOW | Source of truth for 8h tasks | Cáo/Automation | Make append/list script |
| Company OS artifact_registry.jsonl | ADOPT | NOW | Evidence source of truth | Cáo/Automation | Require every DONE entry |
| Datasette | TRIAL | PHASE_1 | Upharma data.db web query/export | Bông/Data | Run pilot if data policy ok |
| LangGraph | TRIAL | PHASE_1/2 | Stateful autonomous workflow | Automation | Prototype task state flow |
| n8n/Make/custom queue | TRIAL | PHASE_1 | RFQ/CRM automation | Automation | Choose low-risk skeleton |
| CrewAI | WATCH/TRIAL | PHASE_2 | Department crews | Automation | Test after Company OS stable |
| Microsoft Agent Framework | WATCH | PHASE_2 | Agent orchestration/A2A/MCP | Cáo/Automation | Research integration fit |
| AnythingLLM | TRIAL | PHASE_1 | Private company knowledge assistant / chat with docs | Automation/Cáo | Test ingest company-os/knowledge + memory/areas |
| Dify | TRIAL | PHASE_1/2 | AI app/workflow platform with knowledge base | Automation | Evaluate after AnythingLLM trial |
| RAGFlow | WATCH/TRIAL | PHASE_2 | Document-heavy RAG engine | Automation/Data | Use if docs volume/parsing need grows |
| Khoj | TRIAL_ALT | PHASE_1 | Second brain + custom agents + automations | Cáo | Compare with AnythingLLM |
| mem0 | WATCH | PHASE_2 | Agent memory layer | Cáo/Automation | Consider for long-term agent memory |
| LlamaIndex | WATCH/TRIAL | PHASE_2 | Custom RAG/agent framework | Automation | Use if custom app needed |
| Haystack | WATCH | PHASE_2 | Production RAG pipelines | Automation | Not fastest Phase 1 |
| Qdrant/Weaviate | WATCH | LATER | Vector DB infrastructure | Data/Automation | Avoid manual infra until scale requires |
| Dify | PRIMARY_TRIAL | PHASE_1 | Company OS app/workflow/RAG platform | Automation/Cáo | Build self-host runbook + knowledge assistant + task routing workflow |
| AnythingLLM | FALLBACK_TRIAL | PHASE_1 | Fast private chat-with-docs if Dify setup/workflow too heavy | Automation/Cáo | Keep as fallback KB MVP |
