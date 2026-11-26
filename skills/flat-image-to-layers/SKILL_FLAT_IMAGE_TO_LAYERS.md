# Skill: Flat Image to Editable Layers
Version: 1.1
Trigger: user wants to convert, recreate or revise a flattened image as a modification-friendly Canva design.

## Definition of done
A saved design containing independently editable title, description, date/time/location, CTA, cards and borders; reusable image/photo/decor assets; and a verification report. If import only gives flat/raster results, mark QA_FAILED and describe limitation.

## Workflow
1. Inspect the original at full resolution. Record frame dimensions and bounding boxes.
2. Make layer inventory: BACKGROUND, PHOTO, DECORATIONS, TITLE, SUBTITLE, DESCRIPTION, DATE, TIME, LOCATION, CTA, ICONS.
3. Crop/mask reusable photographic and botanical sections into independent transparent image assets. Preserve original fidelity; avoid inventing visual details.
4. Clean old baked-in lettering from background areas when necessary. Regenerate *only affected local zones* and keep source image for comparison.
5. Rebuild editable text and shapes natively. Keep text separate from cards; icons independent.
6. Assemble in original stacking order with documented coordinates, colors, fonts, and spacing. For HTML-to-Canva imports, use a page with `data-document-role="page"`; do not assume Canva converts every layer.
7. Inspect imported design/page, and where available query element types or edit a test text element. If inspection is impossible, report editability as unverified.
8. Compare render with approved original (title, collage, bottom panels, CTA). Produce discrepancy list.
9. Send draft through Quality Reviewer. No external publishing until explicitly authorized.

## Fidelity and accessibility
Prioritize original layout and recognizable imagery over style reinterpretation. Make all text legible on mobile. Preserve approved branding. Handle unconfirmed dates with TBD; never copy a conflicted weekday into a public invitation.

## Artifacts
`layer-rebuild-spec.md`, cropped images, Canva assembly package, editability report, QA status.

## Honest limitations
Separate raster decoration layers can be moved/resized/replaced but not edited internally as vectors. An exported PNG is not an editable deliverable. Canva imports may combine layers; verification matters.