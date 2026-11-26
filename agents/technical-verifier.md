# Agent role — Technical Verifier v1.0

A deterministic verification role; it is **not a separate LLM**. Invoke scripts before the independent Quality Reviewer for output formats where automated tests exist.

## Inputs
- Assets manifest naming every cutout PNG and intentional rectangular photo.
- Optional structured Canva `read_design(open_transaction=true)` response saved as JSON (must have page elements, not just flattened text).
- Expectation JSON for expected native text/shapes/image layers.

## Run sequence
1. Run `python tools/verify_layers.py --manifest <assets.json> --report <layer-report.json> --previews <previews-dir>`.
2. Inspect preview composites manually/with the Visual Quality Reviewer on white, black, magenta and checkerboard.
3. After Canva import, export/serialize structured `read_design` response and run `python tools/verify_canva.py --design-json <design.json> --expect <expected.json> --report <canva-report.json>`.
4. Test changing/moving an individual element through a draft transaction if supported; discard test edits. A verified count is not an independent move test.
5. Pass reports to `agents/quality-reviewer.md`, which checks semantic object isolation, design fidelity, text, consent and event facts.

## Results
- `FAIL`: any deterministic failure blocks release and triggers targeted repair/recheck.
- `TECHNICAL_PASSED`: machine-test checks succeeded **but human/visual checks remain required**; never automatically mark `QA_PASSED`.
- `NOT_APPLICABLE`: intentional photographic frames are not required to have transparent alpha, but need regular visual QA.
- `UNVERIFIED`: cannot obtain structured Canva data or assets; do not invent a passing result.

Do not change an existing shared Canva design, post/send material, or claim a saved external result without explicit authorization and tool confirmation.
