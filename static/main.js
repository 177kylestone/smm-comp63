// Minimal Leaflet init for MVP
window.addEventListener('load', function() {
  var map = L.map('map').setView([ -41.3, 174.8 ], 12);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19
  }).addTo(map);
});
