# Layer Reconstruction / Isolation Specification (v1.2)

Status: DRAFT
Source image / dimensions: TBD
Target editor: Canva
Approved visual reference: TBD

## Object-by-object inventory
| ID | Subject only | Original bbox (x,y,w,h) | Output file | Mask method | Isolated? | Edges QA | Native/raster | Anchor / z-order |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| leaf-01 | ONE leaf + stem | TBD | assets/isolated/leaf-01.png | alpha mask | TBD | TBD | raster image | TBD |
| bird-01 | bird only | TBD | assets/isolated/bird-01.png | alpha mask | TBD | TBD | raster image | TBD |

## Edited / regenerated subregions
Record only subject-local repair. Never regenerate context around target unless rebuilding the separate background layer.

## Asset QA checklist
- [ ] True RGBA + transparent alpha outside subject
- [ ] No neighboring objects/text/background in the same PNG
- [ ] No opaque rectangle/checkerboard baked into pixels
- [ ] Natural silhouette, no accidental clipping or stray islands
- [ ] No fringing/halos; clean on white/dark/checkerboard backgrounds
- [ ] Frame tightly bounds subject with transparent safe margin
- [ ] Can move/hide independently in Canva without leftover scenery

## Canva composition
| Element | Kind (native text/shape, isolated image, photo) | Position | Reusable? | Verified editable? |
| --- | --- | --- | --- | --- |
| Title | native text | TBD | Yes | TBD |

## Comparison to approved design
Preserved: TBD
Changed intentionally: TBD
Differences/uncertainty: TBD
QA result: QA_FAILED / QA_PASSED
Publication authorization: NOT GRANTED
