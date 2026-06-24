// Service Worker — Farmácia Alpha PWA
var CACHE = 'alpha-v4.95';

self.addEventListener('install', function(e) {
  self.skipWaiting();
});

self.addEventListener('activate', function(e) {
  e.waitUntil(
    caches.keys().then(function(keys) {
      return Promise.all(keys.map(function(k){ return caches.delete(k); }));
    }).then(function(){ return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function(e) {
  // Network-first: sempre busca versão atualizada, cache só como fallback offline
  e.respondWith(
    fetch(e.request, {cache: 'no-store'}).catch(function() {
      return caches.match(e.request);
    })
  );
});
