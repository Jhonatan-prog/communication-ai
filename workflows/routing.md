# Workflow — Agent Routing
## Basic selection
New event -> Event Planner -> requested creative roles -> Quality Reviewer.
Message-only -> Copywriter -> Quality Reviewer.
E-card -> Visual Designer -> Quality Reviewer.
Video -> Video Producer -> Quality Reviewer.
Revision -> role that owns affected output -> Quality Reviewer.
Multi-channel campaign -> Event Planner creates brief; Copywriter, Visual Designer and Video Producer independently draft; Quality Reviewer checks integrated assets.
## Context strategy
Read AGENTS.md and only relevant agents, templates and knowledge. Load canonical event brief when present. Avoid loading all docs for every task.
## Decision
Keep everything in DRAFT until QA passes. After QA, request approval. No external send, publication or modification without explicit authorization.
## Dependencies
Changes to confirmed place, date, hour or participant rules trigger a re-review of all public materials using those facts.

## Verification routing (v1)
E-card / editable Canva / image-layer reconstruction -> Visual Designer -> Technical Verifier -> Quality Reviewer -> User approval. For message-only or non-layered video requests, use Quality Reviewer without irrelevant PNG/Canva checks. Technical Verifier is a script-driven role, not a permanent autonomous agent.
