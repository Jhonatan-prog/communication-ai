# Verification Pipeline v1.0

Creator -> Technical Verifier -> Visual Quality Reviewer -> User Approval -> Separate Authorized Distribution.

## Gate 1 — Technical checks (deterministic)
For isolated cutouts, require real PNG/RGBA, transparent pixels, non-empty alpha silhouette, transparent inset margins and no nearly-opaque rectangular patch. Flag suspicious disconnected components for visual review. Generate diagnostic white/black/magenta/checkerboard previews. Check Canva structured elements contain independent native text/shapes/media layers, not a single flattened poster.

Inputs: `assets.json`, optional `canva-design.json`, `canva-expectations.json`.
Outputs: JSON reports under `events/<slug>/qa/` with asset-level findings.

## Gate 2 — Visual QA (semantic judgement)
Verify one intended object per isolated asset (no other leaf, building or bird), no halo/edge damage, full design fidelity, alignment, mobile readability, confirmed logistics and the correct source brand/reference. Test actual independent movement/hiding in Canva where possible; Canva reports alone do not prove it.

## Error loop
FAIL -> locate failing asset/field -> only repair that component -> rerun technical test -> rerun affected visual QA. Never regenerate entire approved design for a small problem.

## Status and scope
Machine results are `FAIL` or `TECHNICAL_PASSED`, not `QA_PASSED`. Quality Reviewer alone assigns final `QA_FAILED` / `QA_PASSED`; user approves later and separately authorizes publishing. If scripts/tool data unavailable, report `UNVERIFIED` and block claims of verified editability.

## Execution
`python -m pip install -r requirements-verification.txt`
`python -m unittest discover -s tests -v`
`python tools/verify_layers.py --manifest events/example/qa/assets.json --report events/example/qa/layers.json --previews events/example/qa/previews`
`python tools/verify_canva.py --design-json events/example/qa/canva-design.json --expect events/example/qa/canva-expectations.json --report events/example/qa/canva.json`

### Example asset manifest
```json
{"assets":[{"id":"leaf-01","path":"assets/isolated/leaf-01.png","kind":"cutout"},{"id":"venue","path":"assets/venue.png","kind":"photo"}]}
```

### Example Canva expectations
```json
{"minimum":{"native_text":6,"native_shapes":4,"image_layers":3},"required_text":["LA BARQUEREÑA","Casa de la Cultura"]}
```

Thresholds are examples; derive expected minimums from actual design specification. Photos marked `photo` bypass alpha checks by design.

## v1.3 reference fidelity
Before Technical Verifier, lock the exact input source file (dimensions + SHA256) and inventory mandatory object features. Technical Verifier checks alpha integrity and native Canva layers; visual reviewer additionally checks completeness and nonduplication against the original. Use a temporary Canva move/edit transaction and discard it. Publish status only after all required layers and event facts pass; incomplete object reconstruction remains QA_FAILED.
