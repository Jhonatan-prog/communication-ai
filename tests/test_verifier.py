"""Self-contained synthetic examples; run: python -m unittest discover -s tests -v"""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from verify_layers import inspect_cutout, verify_manifest
from verify_canva import verify


class TestCutout(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def sample(self, name='leaf.png', mode='RGBA', edge=False, patch=False):
        image = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.ellipse((20, 15, 80, 85), fill=(40, 110, 50, 255))
        if edge:
            image.putpixel((0, 50), (40, 110, 50, 255))
        if patch:
            draw.rectangle((2, 2, 97, 97), fill=(255, 255, 255, 255))
        out = self.root / name
        image.convert(mode).save(out)
        return out

    def test_clean_cutout_passes_technical(self):
        r = inspect_cutout(self.sample())
        self.assertEqual(r['status'], 'TECHNICAL_PASSED')
        self.assertTrue(r['requires_visual_review'])

    def test_opaque_rectangular_patch_fails(self):
        r = inspect_cutout(self.sample(patch=True))
        self.assertEqual(r['status'], 'FAIL')

    def test_edge_clipping_fails(self):
        r = inspect_cutout(self.sample(edge=True))
        self.assertIn('insufficient_transparent_margin', r['findings'])

    def test_non_rgba_fails(self):
        r = inspect_cutout(self.sample(mode='RGB'))
        self.assertIn('not_rgba', r['findings'])

    def test_manifest(self):
        self.sample()
        manifest = self.root / 'assets.json'
        manifest.write_text(json.dumps({'assets': [{'id': 'leaf-01', 'path': 'leaf.png', 'kind': 'cutout'}]}))
        self.assertEqual(verify_manifest(manifest)['status'], 'TECHNICAL_PASSED')


class TestCanva(unittest.TestCase):
    def test_structured_layers(self):
        payload = {'design_content': {'pages': [{'isEditable': True, 'elements': [
            {'type': 'text', 'textRegions': [{'characters': 'La Barquereña'}]},
            {'type': 'shape', 'paths': [{'fill': {'color': '#fff'}}]},
            {'type': 'shape', 'paths': [{'fill': {'media': {'type': 'image'}}}]}
        ]}]}}
        result = verify(payload, {'minimum': {'native_text': 1, 'native_shapes': 1, 'image_layers': 1},
                                  'required_text': ['La Barquereña']})
        self.assertEqual(result['status'], 'TECHNICAL_PASSED')
        self.assertTrue(result['requires_visual_review'])

    def test_flattened_poster_fails(self):
        payload = {'design_content': {'pages': [{'isEditable': True, 'elements': [
            {'type': 'shape', 'paths': [{'fill': {'media': {'type': 'image'}}}]}
        ]}]}}
        result = verify(payload, {'minimum': {'native_text': 1}})
        self.assertEqual(result['status'], 'FAIL')


if __name__ == '__main__':
    unittest.main()
