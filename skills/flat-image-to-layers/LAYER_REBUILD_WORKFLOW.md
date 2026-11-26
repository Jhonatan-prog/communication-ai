# Workflow — Object Isolation Before Layer Assembly (v1.2)

## Phase A: Target identification
1. Confirm original design, desired editable components and what must not change.
2. Inventory each **individually separable object**, even when they overlap in the source. Do not define regions only as big rectangles.
3. Record target object ID, semantic boundary, original x/y, visible bbox, occluding objects and intended stacking order.

## Phase B: Alpha-matte extraction
4. Make a crop *for processing*, with enough context to segment; this is NOT yet the exported layer.
5. Create object-specific alpha mask; remove neighboring shapes, leaves, sky, text, paper texture etc. Mask gaps and holes correctly.
6. Decontaminate edge RGB and clean fringing; preserve fine stems and natural soft edges.
7. If original object is partly occluded, fill only hidden parts necessary to move it independently, or flag for review. Never incorporate surrounding sections as a shortcut.
8. Compute nontransparent alpha bounds; trim/canvas-pad by small transparent margin; export `assets/isolated/<id>.png` in RGBA.

## Phase C: Isolated asset QA (required before assembly)
9. Validate PNG alpha, transparent corners/margins, visible silhouette, no neighbor contamination.
10. Inspect on transparent checkerboard, white, black and saturated backdrop at 100% / 200%.
11. Reject dirty layers. Repeat extraction or ask for improved asset. Never import a failed layer as if production-ready.

## Phase D: Assembly and verification
12. Recreate background separately; rebuild all text and geometric panels as editable native Canva items.
13. Import each isolated asset independently with original anchor/size/z-index. A photo rectangle may intentionally remain rectangular.
14. Inspect Canva elements; test independent move/hide and native text editability when tools allow.
15. Compare exported visual to approved reference; record limitations; run Quality Reviewer and obtain approval before shared-asset edits or publishing.

## Mandatory decision examples
- Request “isolate leaf”: export ONLY that leaf + connected stem. Bird, other leaves, paper texture and building are alpha=0.
- Request “isolate bird”: no branch/foliage unless user explicitly wants them attached. Natural legs/feet remain; repair hidden feet only when appropriate and labeled.
- Object + bad crop: QA_FAILED (cannot treat a rectangular screenshot patch as an isolated layer).
- Source too small / edges indeterminate: do not fake source fidelity; mark NEEDS_MANUAL_REVIEW or propose a clearly labeled regenerated single-object PNG.
