# Technical + Visual Verification (v1)

The Communication AI Visual Designer must run **two gates** for layered e-cards:

1. **Technical Verifier**: run the Python scripts in `tools/` on isolated PNG cutouts and structured Canva design JSON. These detect missing transparency, crops reaching edges, near-opaque rectangles, missing native text/shape elements and other measurable issues.
2. **Quality Reviewer**: inspect the diagnostic previews and Canva page for semantic contamination, accurate design fidelity, clean cutout edges and correctness of event facts. Only this reviewer may report `QA_PASSED` after both gates succeed.

## Install and run
```bash
python -m pip install -r requirements-verification.txt
python -m unittest discover -s tests -v
python tools/verify_layers.py --manifest path/to/assets.json --report path/to/layer-report.json --previews path/to/previews
python tools/verify_canva.py --design-json path/to/canva.json --expect path/to/expectations.json --report path/to/canva-report.json
```

`canva.json` must contain **structured** output from Canva `read_design` with an open transaction. It does not authenticate to Canva or trigger a remote edit. For object-only verification, a machine cannot prove that a semitransparent leaf silhouette contains no unwanted pixels from a different leaf — the human/visual pass remains mandatory.

This is a runnable local/CI component, **not an already-deployed n8n workflow**.
