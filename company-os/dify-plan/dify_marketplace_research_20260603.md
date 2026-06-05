# Dify Marketplace — nghiên cứu ứng dụng/templates/plugin có sẵn (2026-06-03)

Nguồn đã kiểm:
- Marketplace web: https://marketplace.dify.ai/templates (browser snapshot, trang JS)
- Official plugins repo: https://github.com/langgenius/dify-official-plugins (clone /tmp, đọc manifests)
- Local Dify: endpoint marketplace cần token console; public template web đọc được.

## 1. Marketplace có những loại gì
Dify Marketplace không chỉ là "app". Có 4 nhóm chính:
1. Templates: app/workflow/chatflow mẫu có thể remix/import.
2. Plugins - Models: nhà cung cấp model như OpenAI, Anthropic, Gemini, DeepSeek, Groq, Ollama/LocalAI/GPUStack, OpenAI-compatible...
3. Plugins - Tools/Datasources: Google Drive, Notion, GitHub, Slack, Discord, Tavily, Jina, Firecrawl, Gmail, Excel, YouTube, Wikipedia, DuckDuckGo, Chart, JSON Process...
4. Agent Strategies/Extensions: CoT agent, webhook, Slack bot, OpenAI-compatible extension.

## 2. Templates nổi bật thấy trực tiếp trên Marketplace
### Dify 101 / cơ bản
- Chatflow Basic: Chatbot — chatbot có memory.
- Workflow Basic: Business Card Reader — OCR/convert card sang dữ liệu.
- Question Classifier: Front Desk Receptionist — phân loại intent và route tới agent.
- Knowledge Retrieval: A Smart Chatbot — chatbot trả lời từ KB.
- Tool: Daily News Digest — tóm tắt tin theo chủ đề.
- Agent & Template: Market Research Agent — nhập website công ty -> báo cáo market research.
- Doc Extractor: AI Summarizer — upload file -> summary.
- Code: UTM Link Builder — tạo UTM.
- Human Input: Writing Assistant — draft + human review.
- Trigger: Website Health Guard — monitor website.

### Featured / nâng cao
- DeepResearch — loop tìm kiếm web, xác định lỗ hổng tri thức, tổng hợp báo cáo.
- Multi-Question RAG Workflow — tách nhiều câu hỏi, retrieve KB, trả lời có citations.
- work ticket system — webhook ticket, phân loại, retrieve KB, sinh phản hồi, notify Slack/Discord.
- Customer Email Automation — phân loại email + lấy KB + soạn reply.
- Daily AI News Digest / AI News Brief — tự động quét tin + gửi Slack/email.
- Meeting Minutes and Summary — transcript họp -> biên bản.
- Visual Presentation Generator — text dài -> slide deck hình ảnh.
- Web Content Search and Summarization Workflow — Tavily + Jina Reader + summary table.
- SQL Creator — natural language -> SQL theo schema.
- Personalized Memory Assistant — trích preference/facts vào memory.
- Patient Intake Chatbot — hỏi thông tin bệnh nhân dạng multi-turn.
- Sentiment Analysis — batch sentiment JSON.
- Code Interpreter / Code Converter — giải thích/chuyển code.
- YouTube Channel Data Analysis — phân tích kênh YouTube.
- File Translation — dịch tài liệu.

### Marketplace templates rất sát với nhu cầu BÚN/Dropship
- Open-Box Deals Aggregator — tìm open-box/refurbished/clearance deals, output structured product/price/condition/url (TinyFish).
- Amazon Competitor Review Analyzer — input 6 Amazon URLs -> competitive analysis (Bright Data + OpenAI).
- SEO Content Brief Generator — scrape SERP + tạo content brief.
- Pangolinfo Amazon Data Scraper — natural language router + Amazon parsers.
- Pangolinfo AI SERP — export Google AI Mode/SGE results, no LLM.
- Reddit Morning Digest — digest subreddit cho trend research.

### Templates sát Company OS / quản trị agent
- Evidence Layer for AI Agent Actions — ký/verify evidence trail (Asqav). Dùng làm ý tưởng governance, không nhất thiết dùng plugin trả phí.
- Task intake gần nhất: Question Classifier, work ticket system, Customer Email Automation.
- Knowledge/RAG: Knowledge Retrieval + Chatbot, Question Classifier & Knowledge & Chatbot, Multi-Question RAG.
- Webhook Trigger Demo — học cách biến event ngoài thành workflow.

## 3. Official plugins repo — danh mục khả dụng
### Datasources
Google Drive, Notion, GitHub, GitLab, Confluence, SharePoint, OneDrive, Dropbox, Box, AWS S3, Azure Blob, Google Cloud Storage, Tencent COS, Tavily datasource, Jina datasource, Firecrawl datasource, BrightData datasource.

### Models
OpenAI, Anthropic, Azure OpenAI, Gemini, DeepSeek, Groq, Cohere, Mistral, Moonshot, HuggingFace, LocalAI, GPUStack, Bedrock, Qwen/Tongyi, OpenRouter-like providers qua openai-compatible/oaicompat extension, v.v.

### Tools
Slack, Discord, Gmail, Google Calendar, Google Tasks, Google Contacts, GitHub/GitLab, Microsoft Excel 365, YouTube, Wikipedia, DuckDuckGo, Bing, Google search, Tavily/Jina/Firecrawl/Websearch, JSON Process, Chart, OCR (PaddleOCR), transcript, podcast, ComfyUI/image tools, WolframAlpha, Yahoo/AlphaVantage, etc.

## 4. Đề xuất áp dụng cho công ty Minh Cường
### Ưu tiên 1 — dựng Company Knowledge Assistant
Template nên dùng: Knowledge Retrieval + Chatbot hoặc Knowledge Retrieval: A Smart Chatbot.
Lý do: nhanh nhất, đúng nhu cầu hỏi quy tắc/trạng thái/SOP.
Cần: model provider local Ollama hoặc 9router + KB tài liệu nội bộ.

### Ưu tiên 2 — Task Intake / phân việc tự động
Template nên học/copy: Question Classifier: Front Desk Receptionist + work ticket system.
Output mong muốn: JSON {domain, owner, risk, deadline, evidence_required, status}.
Ứng dụng: Henry nhắn việc -> Dify phân loại -> OpenClaw giao Bông/Bún/Cáo/Render.

### Ưu tiên 3 — Evidence Auditor
Template nên học: Evidence Layer for AI Agent Actions + Multi-Question RAG Workflow.
Không cần dùng Asqav trả phí ngay; lấy concept: mọi DONE phải có artifact path/link/log, signature optional.

### Ưu tiên 4 — BÚN dropship research
Templates nên thử:
- Open-Box Deals Aggregator
- Market Research Agent
- SEO Content Brief Generator
- Amazon Competitor Review Analyzer (cẩn trọng Bright Data/API cost)
- Reddit Morning Digest
Kết hợp Crawl4AI local để tránh phụ thuộc Bright Data khi có thể.

### Ưu tiên 5 — Upharma / vận hành
Templates nên học:
- SQL Creator: hỏi dữ liệu data.db bằng ngôn ngữ tự nhiên (phải có guardrail tránh query nguy hiểm).
- Meeting Minutes and Summary: tổng hợp họp/voice.
- Customer Email Automation/work ticket system: xử lý ticket nội bộ/CSKH.

## 5. Cảnh báo chi phí/rủi ro
- Nhiều template dùng plugin/API trả phí: Bright Data, Tavily, OpenAI, Gemini, Slack/Gmail OAuth, Pangolinfo.
- Import template chưa đủ chạy: phải cài plugin + cấu hình key + model + publish.
- Dữ liệu nội bộ đưa vào KB phải kiểm soát quyền truy cập; local Ollama an toàn hơn.
- Marketplace là community: cần review prompt/workflow trước khi chạy với dữ liệu thật.

## 6. Khuyến nghị hành động ngay
Theo AI First, việc xem/import thử template rỗng local là reversible, free, low-risk. Nhưng cấu hình API trả phí hoặc OAuth Gmail/Slack/BrightData cần Henry duyệt.

Roadmap 48h:
1. Import/clone template Knowledge Retrieval + Chatbot (hoặc tự dựng nếu import khó).
2. Cắm Ollama local làm model, tạo KB tối thiểu từ DASHBOARD + ACTIVE_RULES + Dify guide.
3. Tạo Task Intake workflow theo mẫu Question Classifier.
4. Tạo BÚN research workflow từ Market Research Agent + Crawl4AI local, chưa dùng API trả phí.

## 7. Status
- Marketplace research: DONE.
- Official plugin categories: DONE.
- Template shortlist cho công ty: DONE.
- Import/test template local: NOT_STARTED.
