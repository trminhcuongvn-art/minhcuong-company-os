# LLM Knowledge Optimization — 2026-06-03

## Decision
Use LLM/RAG for retrieval and synthesis, not fine-tune a company LLM in Phase 1.

## Recommended stack
1. Structured source of truth: Company OS Knowledge Base markdown/jsonl.
2. Semantic search / embeddings: index knowledge, memory, artifacts, decisions.
3. RAG assistant: answer questions with citations to paths.
4. Optional graph layer: link decisions -> tools -> phases -> tasks -> artifacts.
5. Fine-tune only later if repeated task style/classification needs it.

## Why not train/fine-tune now
- Data is still small and changing fast.
- Main pain is retrieval/organization, not model capability.
- Fine-tuning can encode stale decisions.
- RAG is easier to update, verify, and rollback.

## Phase 1 MVP
- Keep markdown/jsonl indexes.
- Add embeddings search over company-os/knowledge + memory/areas.
- Require every answer to cite source path.
- Add tags: product, department, phase, status, owner, decision.

## Future
- If knowledge grows > thousands of docs: vector DB + graph DB.
- If processes stabilize: fine-tune small classifier/router for task triage.
