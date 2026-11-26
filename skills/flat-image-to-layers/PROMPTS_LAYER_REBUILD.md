# Layer Isolation Prompts (v1.2)

## One clean leaf
"Using the flat-image-to-layers skill, extract just the leaf I marked. Export a tightly framed RGBA PNG with all background, other leaves, branches not belonging to it, text and scenery fully transparent. Check all edges on light and dark backgrounds. Do not output a rectangular screenshot crop."

## One bird
"Isolate the bird as its own transparent PNG. Do not include surrounding branch, leaves, building, or paper texture. Restore object-local hidden portions only if necessary and mark any synthesized parts. Reject halos."

## Entire invitation to Canva
"Reconstruct this e-card into individual Canva elements. First make one transparent PNG per distinct decorative object (not one PNG per rectangular visual region); pass per-asset alpha and edge QA; then rebuild title/date/time/location/CTA as native text and shapes. Preserve approved composition. Report editability honestly."

## Check a failed crop
"Audit assets/isolated/ for background contamination, unrelated objects, rough masks, clipped edges and opaque rectangles. Mark every failed asset QA_FAILED and specify the exact cleanup before Canva import."
