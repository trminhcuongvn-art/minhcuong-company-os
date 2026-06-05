# SMB RAG / Knowledge System Options — GitHub Research 2026-06-03

## Goal
Find an optimal knowledge/RAG solution for a small business: easy setup, searchable company knowledge, citations, multi-user, agent/workflow potential, low maintenance.

## Options reviewed

### 1. AnythingLLM — https://github.com/Mintplex-Labs/anything-llm
- Fit: Very strong for small business.
- Pros: local-first, desktop/server, multi-user, document chat, built-in agents, vector DB/document pipeline, low setup friction.
- Cons: less custom workflow/state-machine control than building with LangGraph/LlamaIndex.
- Recommendation: ADOPT/TRIAL for Phase 1 company knowledge assistant.

### 2. Dify — https://github.com/langgenius/dify
- Fit: Strong if we need production app builder + workflows + agents.
- Pros: self-host, visual app/workflow builder, knowledge base, API, team-friendly.
- Cons: heavier than AnythingLLM; more platform setup.
- Recommendation: TRIAL Phase 1/2 for external/internal AI apps.

### 3. RAGFlow — https://github.com/infiniflow/ragflow
- Fit: Strong for document-heavy RAG.
- Pros: RAG engine with agent capabilities; good context layer; document parsing focus.
- Cons: heavier; likely overkill for current markdown/jsonl knowledge base.
- Recommendation: WATCH/TRIAL Phase 2 if document volume grows.

### 4. Open WebUI — https://github.com/open-webui/open-webui
- Fit: Good chat UI for local/cloud LLMs.
- Pros: user-friendly interface, Ollama/OpenAI compatible.
- Cons: knowledge/workflow is not as business-KB focused as AnythingLLM/Dify.
- Recommendation: WATCH or use as general LLM UI, not core KB.

### 5. Khoj — https://github.com/khoj-ai/khoj
- Fit: Good as personal/team second brain and automations.
- Pros: docs/web answers, custom agents, scheduled automations, semantic search, self-hostable.
- Cons: may overlap with AnythingLLM; need compare setup/integration.
- Recommendation: TRIAL alternative to AnythingLLM.

### 6. mem0 — https://github.com/mem0ai/mem0
- Fit: Agent memory layer, not full SMB KB UI.
- Pros: universal memory layer for agents; good for long-term agent personalization/facts.
- Cons: not enough alone; needs app/RAG layer.
- Recommendation: WATCH/TRIAL as agent memory add-on.

### 7. LlamaIndex — https://github.com/run-llama/llama_index
- Fit: Strong developer framework for custom RAG/agent apps.
- Pros: flexible indexing, agentic apps, parsing/OCR ecosystem.
- Cons: needs development work; less plug-and-play.
- Recommendation: Use when custom Company OS RAG app is needed.

### 8. Haystack — https://github.com/deepset-ai/haystack
- Fit: Strong production RAG/orchestration framework.
- Pros: modular pipelines, retrieval/routing/memory/generation control.
- Cons: developer-heavy.
- Recommendation: WATCH for production pipeline, not Phase 1 fastest path.

### 9. Qdrant / Weaviate
- Fit: Vector DB infrastructure.
- Pros: scalable vector search, metadata filtering.
- Cons: DB only, not full KB product.
- Recommendation: use only if AnythingLLM/Dify built-ins are insufficient.

## Recommendation for Minh Cường
Best Phase 1 path for small business:
1. ADOPT/TRIAL AnythingLLM as fastest private company knowledge assistant.
2. In parallel, keep Company OS markdown/jsonl as source of truth.
3. Evaluate Dify as Phase 1/2 app/workflow platform if we need internal apps and agent workflows.
4. Use LlamaIndex/LangGraph only for custom Company OS automation/state machine, not as first KB UI.
5. Avoid building vector DB infra manually now.

## Acceptance criteria for trial
- Can ingest company-os/knowledge + memory/areas.
- Answers cite source files/paths.
- Supports multiple workspaces/users or at least separate workspaces by department.
- Allows local/cloud LLM provider selection.
- Has API or integration path for agents.
- Setup time < 1 block.
- Rollback easy: remove container/app; source files remain unchanged.
