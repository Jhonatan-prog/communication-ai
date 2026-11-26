# La Barquereña — Clean Isolation Regression Case
Status: DRAFT, retest required
Reference: approved cream/forest-green botanical e-card, original building image, leaves, bird, three logistic cards, footer CTA.

## Why previous test was insufficient
Prior Canva import verified separately editable text/shapes but some decorative PNG assets contained rectangular portions of the surrounding poster. Thus overall canvas editability passed while **cutout cleanliness was not verified**. This new test explicitly fails any decorative image with background contamination.

## Isolation targets
| File | Only intended content | Must be transparent |
| --- | --- | --- |
| `leaf-left-01.png` | one left leaf with its own connected stem | paper, other leaves, building, text |
| `leaf-left-02.png` | second distinct left leaf | all other content |
| `flower-01.png` | flower and natural connected detail | surrounding foliage/background |
| `bird-01.png` | bird (legs and feet included) | branch, neighboring leaf, background |
| `leaf-right-01.png` | one right leaf | bird, other leaves, background |
| `leaf-bottom-01.png` | bottom leaf only | source poster corners/text |
| `venue-photo.png` | intentional rectangular venue photo | photo frame may be rectangular |

Group leaves into one branch only when explicitly requested and still export a transparent silhouette.

## Canva reconstruction
- Cream page background independent
- Each cleaned PNG independent and moveable; original approximate coordinates/z-index
- Main title and subtitle as native text
- Subtitle outline, cards, CTA pill as native shapes
- Date/time/location as separate editable text; unconfirmed date and hour remain TBD
- Verify moving a single leaf doesn't drag along a sky/cream patch or other leaf

## QA criteria
1. Inspect every PNG with alpha, bbox and diagnostic backdrop.
2. Reject partial rectangular patches, nearby objects, halos, clipped tips or spill.
3. Import only assets passing tests.
4. Inspect Canva element types and compare reconstructed layout to original.
5. Reconstruct only object-local occlusions; label any generated parts.
Current existing Canva test `DAHcCx3O-us` is not retroactively fixed; a new clean-isolation rebuild is needed to claim complete success.
