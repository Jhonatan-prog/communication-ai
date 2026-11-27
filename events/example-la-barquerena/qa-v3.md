# La Barquereña — Canva v3 QA
Status: QA_FAILED / DRAFT, not public-ready

## Source and output
- Source: user-uploaded `image(1).png` (1122 × 1402), SHA256 `eb010bcfd34ab2b261d109e02a2687b1054c09917f91d1df7e3ce595f0130666`
- Canva: https://www.canva.com/d/dJ1Mq6afKBsfRgf (design ID `DAHcIYvfqe0`)
- Existing prior Canva files not overwritten.

## Tests
- Local alpha integrity: 16 subject PNGs, margins and RGBA checked, 16/16 passed measurable criteria.
- Canva structure: 44 elements; 8 editable text; 17 independent image elements, plus native shapes.
- Date text changed independently; bird moved independently; read-back confirmed; both changes discarded.

## Remaining QA failures
- Some isolated botanical elements still contain original scenery pixels or missing delicate details.
- Bird silhouette is now complete, but tiny feathers/feet and green matte edges differ from source.
- Venue collage was selectively inpainted behind bird; hidden original scene cannot be recovered precisely.
- Typeface approximated, not a pixel-exact match.
- Example original date/weekday not confirmed: `Sábado 15 de noviembre`, `9:00 a.m.`; 2026-11-15 was Sunday.

**Disposition:** Functional editability verified; visually not exactly identical. Further targeted repairs required before QA_PASSED. Never post based on this example.