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

## Reconstruction test v3 — 27 November 2026
- Exact source: user's `image(1).png`, 1122 × 1402, SHA256 `eb010bcfd34ab2b261d109e02a2687b1054c09917f91d1df7e3ce595f0130666`. **Do not substitute `image(9).png`.**
- New Canva draft ID: `DAHcIYvfqe0`; edit link: https://www.canva.com/d/dJ1Mq6afKBsfRgf
- Structural check: 44 elements total, including 8 native text elements and 17 separate image-backed layers (paper background + 16 isolated assets). Card backgrounds/shapes are separate.
- Local transparency/margin checks: 16/16 TECHNICAL_PASSED.
- Actual temporary Canva edit: bird moved from x813 to x850; date replaced; both verified independently; transaction discarded, saved draft unchanged.
- **Visual review status: QA_FAILED** for strict pixel fidelity: some leaf masks contain scenery contamination/eroded details, vegetation under the bird requires local reconstruction, and the font is an editable approximation, not an exact typeface match.
- Original sample “Sábado 15 de noviembre” and “9:00 a.m.” were copied **only** for draft fidelity; not confirmed logistics and Sunday 15 Nov 2026 conflicts with “Sábado”.
- Do not claim final approved/published or exact fidelity. Continue localized cutout cleanup and visual QA.
