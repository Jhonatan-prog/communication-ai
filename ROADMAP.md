# Implementation Roadmap
## Phase 1 — Prompt framework
Keep AGENTS.md, six agent prompts, event templates, QA checklist and Git history. Test manually with sample event. Deliverables are drafts only.
## Phase 2 — Editable creative workflow
Build Canva templates with independent text boxes/shapes and imported imagery. Track Canva design IDs and approved versions. Verify layers and mobile readability.
## Phase 3 — n8n orchestration
Implement event intake -> normalized brief -> role-specific generation -> validation -> human approval -> artifact storage. Reuse schemas/event.schema.json; use least-privilege credentials.
## Phase 4 — Authorized distribution
Connect supported scheduling and messaging providers, implement audit log, explicit publish authorization, retry/idempotency and post-event review. Never bypass approvals.
## Exit tests
No invented logistics; reproducible templates; QA catches incorrect weekday; edits preserve design; no external side effects without permission.
