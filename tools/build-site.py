#!/usr/bin/env python3
"""Build the deployable site/ folder from index.html.

Usage: python3 tools/build-site.py

- replaces the Google Fonts links with the self-hosted fonts in site/fonts/
- adds the favicon, the web app manifest and the service worker registration
- stamps the service worker cache name so browsers pick up the new version
"""
import hashlib
import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'index.html').read_text(encoding='utf-8')

html, n = re.subn(
    r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\n'
    r'<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\n'
    r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2[^"]*">\n',
    '<meta name="description" content="Audio Companion : comparaison A/B de fichiers audio, suivi des projets et détecteur de masquage. Tout se passe dans le navigateur.">\n'
    '<meta name="theme-color" content="#000000">\n'
    '<link rel="icon" href="favicon.svg" type="image/svg+xml">\n'
    '<link rel="manifest" href="manifest.webmanifest">\n'
    '<link rel="stylesheet" href="fonts/fonts.css">\n',
    src,
)
assert n == 1, 'Google Fonts block not found in index.html'

sw_register = '''<script>
if ('serviceWorker' in navigator && window.isSecureContext) {
  window.addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));
}
</script>
</body>'''
assert html.count('</body>') == 1
html = html.replace('</body>', sw_register)

(root / 'site' / 'index.html').write_text(html, encoding='utf-8')

build = hashlib.sha256(html.encode('utf-8')).hexdigest()[:10]
sw_path = root / 'site' / 'sw.js'
sw = sw_path.read_text(encoding='utf-8')
sw = re.sub(r"const CACHE = '[a-z-]*-[0-9a-f]+';|const CACHE = '[a-z-]*__BUILD__';", f"const CACHE = 'audio-companion-{build}';", sw)
sw_path.write_text(sw, encoding='utf-8')
print(f'site/index.html written (build {build})')
