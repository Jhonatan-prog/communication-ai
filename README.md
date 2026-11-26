# Communication AI — v1.0

Human-approved multi-agent communication framework for community and youth events.

## Quick start
1. Read `AGENTS.md` and `agents/orchestrator.md`.
2. Copy `templates/event-brief.md` into `events/<event-slug>/brief.md`.
3. Use `workflows/new-event.md` to create event deliverables.
4. Run `agents/quality-reviewer.md` and `workflows/approval.md` before any publishing.

Agents are logical roles, not automatically running services. Canva editing, GitHub writes and outbound publishing require supported integrations and appropriate authorization. Event logistics that are not confirmed remain `TBD`.

See `ROADMAP.md`, `integrations/n8n/README.md`, and `examples/routing-cases.md` for future integration.

## Technical verification
Use `README_VERIFICATION.md` for machine checks and visual review. Install Pillow with `pip install -r requirements-verification.txt` and run `python -m unittest discover -s tests -v`. Layered Canva reconstruction requires both verification gates.
