# Technical + Visual Verification (v1)

Communication AI uses two verification gates for layered e-cards **after the artifact is produced**, initiated by the Communication Orchestrator rather than by GitHub repository events.

1. **Technical Verifier:** Run Python scripts in `tools/` against isolated PNG layers and structured Canva design JSON. Check actual transparency, inset margins, suspect rectangular crops, and native text/shape/image elements.
2. **Quality Reviewer:** Inspect diagnostic previews and the Canva design for subject-only isolation, fidelity, clean edges, event accuracy and true modification readiness. Only this reviewer can assign `QA_PASSED` after both gates succeed.

## Run when producing an output

```bash
python -m pip install -r requirements-verification.txt
python -m unittest discover -s tests -v
python tools/verify_layers.py --manifest path/to/assets.json --report path/to/layer-report.json --previews path/to/previews
python tools/verify_canva.py --design-json path/to/canva.json --expect path/to/expectations.json --report path/to/canva-report.json
```

`canva.json` must contain **structured** output from Canva `read_design` with an open editing transaction; text-only output is not sufficient. The scripts do not authenticate to Canva or perform remote changes. An alpha mask alone cannot prove that an isolated object contains no contamination; the independent visual review remains mandatory.

GitHub stores the agent instructions, workflow descriptions, scripts and tests, but **does not execute QA**. ChatGPT or another capable orchestrator runs relevant checks at artifact-production time where supported. When execution or Canva inspection is unavailable, report `UNVERIFIED` instead of claiming a passing result. Future n8n orchestration remains optional and is not deployed.
