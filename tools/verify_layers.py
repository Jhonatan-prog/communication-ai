#!/usr/bin/env python3
"""Deterministic checks for isolated RGBA PNG cutouts. Does not replace visual QA."""
import argparse
import json
from pathlib import Path
from PIL import Image


def inspect_cutout(path, min_margin=2):
    findings = []
    metrics = {}
    try:
        with Image.open(path) as opened:
            metrics['format'] = opened.format
            metrics['mode'] = opened.mode
            if opened.format != 'PNG':
                findings.append('not_png')
            if opened.mode != 'RGBA':
                findings.append('not_rgba')
            img = opened.convert('RGBA')
    except (OSError, ValueError) as exc:
        return {'path': str(path), 'status': 'FAIL', 'findings': ['unreadable_image: ' + str(exc)], 'metrics': {}}

    width, height = img.size
    metrics['size'] = [width, height]
    if width < 8 or height < 8:
        findings.append('image_too_small')
    alpha = img.getchannel('A')
    lo, hi = alpha.getextrema()
    if lo == 255:
        findings.append('no_transparent_pixels')
    if hi == 0:
        findings.append('empty_cutout')
    bbox = alpha.getbbox()
    metrics['alpha_bbox'] = list(bbox) if bbox else None
    if bbox:
        left, top, right, bottom = bbox
        metrics['margins_px'] = [left, top, width - right, height - bottom]
        if min(metrics['margins_px']) < min_margin:
            findings.append('insufficient_transparent_margin')
        coverage = sum(alpha.histogram()[1:]) / (width * height)
        metrics['nonzero_alpha_fraction'] = round(coverage, 4)
        if coverage > 0.92:
            findings.append('almost_full_rectangle_possible_background')
        # Multiple components are a review warning, not proof of error.
        if width * height <= 4_000_000:
            pixels = alpha.point(lambda p: 255 if p > 20 else 0).tobytes()
            visited = bytearray(width * height)
            components = []
            for start, value in enumerate(pixels):
                if value == 0 or visited[start]:
                    continue
                stack = [start]
                visited[start] = 1
                count = 0
                while stack:
                    ix = stack.pop()
                    count += 1
                    x, y = ix % width, ix // width
                    for nxt in (ix - 1 if x else -1, ix + 1 if x + 1 < width else -1,
                                ix - width if y else -1, ix + width if y + 1 < height else -1):
                        if nxt >= 0 and not visited[nxt] and pixels[nxt] != 0:
                            visited[nxt] = 1
                            stack.append(nxt)
                components.append(count)
            components.sort(reverse=True)
            metrics['connected_components'] = len(components)
            if len(components) > 1 and components[1] >= max(9, components[0] * 0.01):
                findings.append('review_disconnected_foreground_components')
        else:
            findings.append('component_check_skipped_large_image')
    else:
        metrics['margins_px'] = None
    # Alpha alone cannot prove that the correct object is isolated.
    hard_fail = {'not_png', 'not_rgba', 'no_transparent_pixels', 'empty_cutout',
                 'image_too_small', 'insufficient_transparent_margin',
                 'almost_full_rectangle_possible_background'}
    status = 'FAIL' if hard_fail.intersection(findings) else 'TECHNICAL_PASSED'
    return {'path': str(path), 'status': status, 'findings': findings,
            'metrics': metrics, 'requires_visual_review': True}


def make_previews(path, directory):
    directory.mkdir(parents=True, exist_ok=True)
    with Image.open(path) as original:
        layer = original.convert('RGBA')
    for name, color in [('white', '#ffffff'), ('black', '#101010'), ('magenta', '#e81e82')]:
        surface = Image.new('RGBA', layer.size, color)
        surface.alpha_composite(layer)
        surface.convert('RGB').save(directory / f'{path.stem}-{name}.png')
    w, h = layer.size
    checker = Image.new('RGB', layer.size, '#eeeeee')
    from PIL import ImageDraw
    draw = ImageDraw.Draw(checker)
    cell = 20
    for y in range(0, h, cell):
        for x in range(0, w, cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, min(w - 1, x + cell - 1), min(h - 1, y + cell - 1)), fill='#bfbfbf')
    checker.paste(layer, (0, 0), layer)
    checker.save(directory / f'{path.stem}-checker.png')


def verify_manifest(manifest_path, preview_dir=None):
    payload = json.loads(Path(manifest_path).read_text(encoding='utf-8'))
    base = Path(manifest_path).parent
    assets = payload.get('assets', [])
    if not isinstance(assets, list) or not assets:
        return {'status': 'FAIL', 'findings': ['manifest_requires_nonempty_assets'], 'assets': []}
    results = []
    for entry in assets:
        asset = base / entry['path']
        kind = entry.get('kind', 'cutout')
        if kind != 'cutout':
            results.append({'path': str(asset), 'kind': kind, 'status': 'NOT_APPLICABLE',
                            'findings': ['intentional_photo_frame_requires_visual_review']})
            continue
        result = inspect_cutout(asset, entry.get('min_margin_px', 2))
        result['id'] = entry.get('id', asset.stem)
        result['kind'] = kind
        results.append(result)
        if preview_dir is not None and result['status'] != 'FAIL':
            make_previews(asset, Path(preview_dir) / result['id'])
    return {'status': 'FAIL' if any(r['status'] == 'FAIL' for r in results) else 'TECHNICAL_PASSED',
            'requires_visual_review': True,
            'limitations': ['Subject identity, background contamination inside the mask, edge halos, and Canva move/hide behavior need visual review.'],
            'assets': results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', required=True, type=Path)
    parser.add_argument('--report', required=True, type=Path)
    parser.add_argument('--previews', type=Path)
    args = parser.parse_args()
    try:
        result = verify_manifest(args.manifest, args.previews)
    except (OSError, KeyError, ValueError, TypeError, json.JSONDecodeError) as exc:
        result = {'status': 'FAIL', 'findings': ['invalid_manifest_or_asset: ' + str(exc)], 'assets': []}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'status': result['status'], 'report': str(args.report)}))
    raise SystemExit(1 if result['status'] == 'FAIL' else 0)


if __name__ == '__main__':
    main()
