# Skill — Flat Image to Clean Editable Layers
Version: 1.2 | Owner: Visual Designer | Status: ACTIVE

## Trigger
Use when asked to convert a flat poster/e-card/image to Canva layers, preserve the original composition during revisions, isolate parts, or regenerate an image asset.

## NON-NEGOTIABLE: one subject, one clean layer
A crop of the source rectangle is **not** an isolated layer. Each object layer MUST show **only its intended subject**, with every pixel outside that object's silhouette transparent. Example: `leaf_01.png` contains that leaf and its natural stem only — no neighboring leaf, bird, building, paper texture, text, sky, or rectangular background. If a bird and a leaf overlap, they require separately isolated assets unless the user explicitly requests the pair as a single decoration.

**Forbidden:** screenshot fragments that reproduce parts of neighboring sections; opaque backgrounds inside decorative assets; leftover lettering; rectangular colored patches; jagged edges, halos/fringing, clipped leaf tips, invented neighboring details, or output called “fully editable” merely because it is a flat PNG.

## What a good layer looks like
- Transparent PNG with actual alpha channel (RGBA), not white/checkerboard pixels baked into the background.
- Frame/bounding box tightly encloses the complete subject, with a small clear margin (default 3–5% of longer object dimension; adapt for thin stems). No visible foreign pixels.
- Preserve original subject silhouette, color, grain and sharpness as far as feasible. Keep the object fully inside the crop, no accidental clipping.
- Edge mask is refined: natural anti-aliasing, no colored halo, pixel noise, detached fragments or background contamination.
- Asset can move, scale or be hidden in Canva without revealing any unwanted section from the original design.
- Separate text and geometric components as native Canva text/shapes, not raster crops.

## Mandatory isolation pipeline (before Canva)
1. **Inventory:** name ONE intended object; note its original bounding box and overlapping neighbors.
2. **Mask:** use foreground segmentation/selection and a refined alpha mask of that object only, including its intended stem/tips and internal holes. A rectangular crop alone never passes.
3. **Remove surrounding content:** all non-object pixels MUST become alpha=0, including distant background and other objects. For overlapping regions, manually subtract neighbors from mask.
4. **Repair selectively:** if another element occludes the object, preserve the visible original; reconstruct only genuinely missing *object-local* pixels when needed, using the original as reference. Do not copy adjacent scenery. If uncertain or not separable, flag `NEEDS_MANUAL_REVIEW`, never hide the defect.
5. **Export:** isolated asset `<object-id>.png` as true RGBA PNG; trim to alpha bounding box + clean margin; retain original design x/y placement metadata.
6. **Inspect:** checkerboard, white, dark, and high-contrast background previews; zoomed edges and full composition. Reject any rectangle, fringe or stray non-object pixel.
7. **Assemble:** import each PNG as an independent Canva image; reconstruct text, cards, icons and CTA as independent editable elements; restore original relative locations.
8. **Verify:** inspect Canva layer types and test moving/hiding one object independently; inspect exported preview for visible defects. Do not save changes to an existing shared design without explicit authorization.

## QA acceptance (all mandatory for a decorative object)
- [ ] One intended subject only; no adjacent sections, letters or unrelated pixels.
- [ ] PNG decodes as RGBA; transparent pixels present outside subject.
- [ ] Outer corners/clear margins fully transparent; visible geometry confined to object silhouette.
- [ ] No solid rectangular backdrop, halos, edge fringing, jaggies, detached pieces or unintentionally cropped tips.
- [ ] Object looks clean on checkerboard AND white/dark/colored backdrops.
- [ ] Object can be moved in Canva without a visible source-background patch.
- [ ] The full recomposed design is faithful to the approved source and typography remains separately editable.
Fail any mandatory item -> `QA_FAILED`; repair/re-segment before claiming the asset is ready.

## Special cases
- Multi-leaf branches: isolate each leaf when individual editing is requested; a decorative branch may be one object **only with user approval** or when it is clearly a single inseparable motif, and must still have a clean transparent silhouette.
- Building/photo: a full photograph may be an intentional rectangular image layer. Only decorative cutouts require alpha isolation; do not remove the background of an image the user wants as a photo.
- Occlusion: exact hidden pixels do not exist in the source. Report any generated completion as reconstructed, never exact source recovery.
- Canva images remain replaceable/positionable raster assets, not internally editable vectors. Do not claim otherwise.

## Deliverables
`layer-rebuild-spec.md`, individual transparent PNGs, subject manifest (source bounds, placement bounds, mask status), preview/contact sheet with diagnostic backgrounds, editable Canva design where supported, and QA/limitations report. No publication without explicit authorization.

## Reference techniques
- Adobe: https://www.adobe.com/products/photoshop/cut-out-an-image.html (selection + non-destructive layer masks and refining)
- PHLEARN: https://phlearn.com/tutorial/isolate-subjects-and-clean-up-edges-in-photoshop/ (video/guide about edge halos)
- Canva: https://www.canva.com/features/background-remover/ (clean cutout and transparent PNG)
