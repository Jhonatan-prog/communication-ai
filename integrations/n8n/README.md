# n8n — Future Integration Blueprint
No active n8n workflow or credentials included in v1.
## Nodes (proposal)
Webhook/form trigger -> validate input against event schema -> create/update canonical brief -> dispatch specialized AI tasks -> consolidate drafts -> QA gate -> human approval -> permitted delivery -> audit log.
## Design principles
- Store stable event ID, version, state, approved_by/at and artifact references.
- Use external systems only with least-privilege tokens from secret storage.
- Deduplicate retries; do not broadcast messages twice.
- Distinguish draft approval from send/publish authorization.
- If confirmed logistics change, invalidate affected assets and trigger re-QA.
- For Canva, use approved editable templates and verify generated design IDs.
- Respect channel policies, privacy and consent.

## Future verification node
When automating, add deterministic asset checks (`tools/verify_layers.py`) and structured Canva checks (`tools/verify_canva.py`) before the Quality Reviewer / human approval gate. Script failures must stop workflow publication and create repair tasks. This repo does not deploy n8n automatically.
