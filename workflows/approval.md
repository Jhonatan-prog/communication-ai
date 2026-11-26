# Workflow — Approval
Stages: DRAFT -> QA_FAILED / QA_PASSED -> APPROVED -> PUBLISHED.
- Creator marks draft status with event ID.
- Quality Reviewer must record pass/fail with issues.
- User approval may advance a draft to APPROVED but does not authorize external actions.
- Explicit separate user authorization is required for send, post, calendar invites, changes to existing shared Canva assets and identifiable footage.
- Publishing action must be logged with destination and exact version; do not claim success before integration confirms.
- Any confirmed logistics change invalidates approval of affected public assets.

## Machine + visual gate
For reconstructed visual assets, require Technical Verifier result `TECHNICAL_PASSED` AND Quality Reviewer `QA_PASSED` before presenting the asset as verified. A missing report is `UNVERIFIED`, never an implicit pass. User approval remains separate from authorization to publish.
