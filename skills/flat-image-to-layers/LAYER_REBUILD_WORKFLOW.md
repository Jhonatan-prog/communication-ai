# Layer Rebuild Execution
1. Detect exact reference and future edits.
2. Measure geometry; record pixel bounding boxes.
3. Segment into independent cropped photo, leaves, bird and other decorative parts; apply transparent masks where possible.
4. Recreate background and geometric cards.
5. Recreate each text block as editable text.
6. Assemble into Canva using supported native design/import capabilities.
7. Verify layer editability, page preview, content fidelity and any missing details.
8. Run QA and return changed/unchanged list.

Decision rules: use original asset over generated imitation when practical; regenerate only missing/dirty regions; prefer real native text/shapes; never describe raster-only import as fully editable.