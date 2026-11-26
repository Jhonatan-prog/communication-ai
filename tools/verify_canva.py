#!/usr/bin/env python3
"""Inspect Canva structured read_design output; not a substitute for interactive edit verification."""
import argparse
import json
from pathlib import Path


def verify(data, expectations):
    if isinstance(data, dict) and isinstance(data.get('text'), str):
        data = json.loads(data['text'])
    content = data.get('design_content', {})
    if isinstance(content, str):
        return {'status': 'FAIL', 'findings': ['requires_structured_design_content_from_open_transaction'], 'counts': {}}
    pages = content.get('pages', [])
    elements = [e for page in pages for e in page.get('elements', [])]
    native_text = [e for e in elements if e.get('type') == 'text']
    native_shapes = [e for e in elements if e.get('type') in ('rect', 'shape') and not any(
        p.get('fill', {}).get('media') for p in e.get('paths', []))]
    images = [e for e in elements if any(p.get('fill', {}).get('media') for p in e.get('paths', []))]
    joined = '\n'.join(''.join(r.get('characters', '') for r in e.get('textRegions', [])) for e in native_text)
    counts = {'pages': len(pages), 'native_text': len(native_text), 'native_shapes': len(native_shapes), 'image_layers': len(images)}
    findings = []
    for field in ['native_text', 'native_shapes', 'image_layers']:
        if counts[field] < expectations.get('minimum', {}).get(field, 0):
            findings.append(f'{field}_below_expected')
    for phrase in expectations.get('required_text', []):
        if phrase not in joined:
            findings.append('missing_text: ' + phrase)
    if not pages or any(page.get('isEditable') is not True for page in pages):
        findings.append('page_editability_not_verified')
    if counts['native_text'] == 0 and counts['image_layers'] > 0:
        findings.append('possible_flattened_poster')
    return {'status': 'FAIL' if findings else 'TECHNICAL_PASSED', 'findings': findings,
            'counts': counts, 'requires_visual_review': True,
            'limitations': ['Does not prove object isolation or successful independent move/hide without a separate controlled Canva edit test.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--design-json', type=Path, required=True)
    parser.add_argument('--expect', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = verify(json.loads(args.design_json.read_text(encoding='utf-8')),
                        json.loads(args.expect.read_text(encoding='utf-8')))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result = {'status': 'FAIL', 'findings': ['invalid_input: ' + str(exc)], 'counts': {}}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'status': result['status'], 'report': str(args.report)}))
    raise SystemExit(1 if result['status'] == 'FAIL' else 0)


if __name__ == '__main__':
    main()
