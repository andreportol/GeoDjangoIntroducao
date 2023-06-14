// Configurações do mapa
var map = L.map('map').setView([-20.4379513, -54.618873], 11);

// Camadas base
var baseLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

// Camadas adicionais (overlays)
var layer = L.geoJson();
map.addLayer(layer);
$getJSON("{% url 'mapa/municipios:municipios_geojson' %}", function(data){
  layer.addData(data);
})




// Adicionar a camada base ao mapa
baseLayer.addTo(map);
