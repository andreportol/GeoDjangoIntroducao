// Configurações do mapa
var map = L.map('map').setView([-20.4379513, -54.618873], 11);
// Camadas base
var baseLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

// Camadas adicionais (overlays)
// configuração do polígono
var myStyle = {
  fillColor:'white',
  weight: 2,
  opacity: 1,
  color: 'blue',
  fillOpacity: 1
}

var municipios_geojson_dataurl = $("#municipios_geojson").val(); // recupera o valor da URL, onde o id é municipios_geojson
//var municipiosLayer = L.geoJSON([],myStyle).addTo(map);// cria uma camada vazia e adiciona ao mapa

var municipiosLayer = L.geoJSON(null, {
  style:myStyle,// chamando a configuração dos shapefiles
  onEachFeature: function(feature, layer) {
    var popupContent = feature.properties.popup_content;
    layer.bindPopup(popupContent);
  }
}).addTo(map);

$.getJSON(municipios_geojson_dataurl, function(data) {
  municipiosLayer.addData(data);
});
/*
var overlays = {
  "Municipios": municipios,
}

*/


// Adicionar a camada base ao mapa
baseLayer.addTo(map);




