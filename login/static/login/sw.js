function cacheAssets() {
  return caches.open('cache-v1')
  .then(function(cache) {
    return cache.addAll([
      '.',
      'register.html',
      'login/style.css',
      'loginn.html',
      'display.html',
      'login/script.js'
    ]);
  });
}



self.addEventListener('install', function(event) {
  event.waitUntil(
    cacheAssets()
  );
});




self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      // Check cache but fall back to network
      return response || fetch(event.request);
    })
  );
});