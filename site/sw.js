// Offline support: the page and its fonts are cached so Audio Companion opens without a connection.
// The page itself is fetched network-first, so a new upload on the server is picked up on the next visit.
const CACHE = 'audio-companion-dec93f85e1';
const SHELL = [
  './',
  'favicon.svg',
  'manifest.webmanifest',
  'fonts/fonts.css',
  'fonts/inter-tight-latin-300-normal.woff2',
  'fonts/inter-tight-latin-400-normal.woff2',
  'fonts/inter-tight-latin-500-normal.woff2',
  'fonts/inter-latin-300-normal.woff2',
  'fonts/inter-latin-400-normal.woff2',
  'fonts/inter-latin-500-normal.woff2',
  'fonts/ibm-plex-mono-latin-400-normal.woff2',
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => (k.startsWith('comparo-') || k.startsWith('audio-companion-')) && k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  if (req.mode === 'navigate') {
    e.respondWith(
      fetch(req)
        .then(res => { const copy = res.clone(); caches.open(CACHE).then(c => c.put('./', copy)); return res; })
        .catch(() => caches.match('./'))
    );
    return;
  }
  e.respondWith(caches.match(req).then(hit => hit || fetch(req)));
});
