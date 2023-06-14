// Configurações do mapa
var map = L.map('map').setView([-20.4379513, -54.618873], 11);
// Camadas base
var baseLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

// Camadas adicionais (overlays)
var municipios_geojson_dataurl = $("#municipios_geojson").val();
var municipiosLayer = L.geoJSON().addTo(map);

$.getJSON(municipios_geojson_dataurl, function(data) {
  municipiosLayer.addData(data);
});


// Adicionar a camada base ao mapa
baseLayer.addTo(map);




