# Test — Clean Object Isolation (v1.2)

## Acceptance fixture
Given the La Barquereña original e-card, when extracting one leaf, bird or flower:

### File checks
- [ ] `PNG` format and `RGBA` alpha channel
- [ ] Nonzero transparent pixels; no opaque checkerboard
- [ ] All four corner pixels transparent unless valid silhouette clearly touches a specific cropped corner (then add margin)
- [ ] Nontransparent alpha bbox is contained inside full PNG with small transparent margin
- [ ] No other subject/background/text visible in diagnostic previews
- [ ] Natural anti-aliased edges with no pale/green fringes or stray fragments
- [ ] Leaf stem and tips not unintentionally cut off
- [ ] Saved scale/original placement metadata

### Viewer/editor checks
- [ ] White + dark + saturated + checkerboard preview clean
- [ ] Moving an individual object in Canva does not expose a copied rectangular poster patch
- [ ] Independent layers for bird vs leaf vs photo vs decorations
- [ ] Title/date/time/location/CTA remain independent native text
- [ ] QA rejects *visually acceptable composite* when an individual asset is dirty

## Failure conditions
Opaque rectangular source crop, unrelated pixels, accidental clipping, nontransparent halo, wrong grouped objects or imported flat poster => QA_FAILED.

## Notes
Alpha tests are necessary but not sufficient: a non-transparent unrelated leaf inside alpha silhouette still fails semantic inspection. Human/image-model visual inspection remains mandatory.
