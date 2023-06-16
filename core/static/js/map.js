// Configurações do mapa
var map = L.map('map').setView([-20.4379513, -54.618873], 11);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Variável para armazenar o marcador
var marker;

// Função para adicionar o marcador no mapa
function addMarkerToMap(latitude, longitude) {
  // Remover o marcador existente (se houver)
  if (marker) {
    map.removeLayer(marker);
  }

  // Criar novo marcador na posição desejada
  marker = L.marker([latitude, longitude], { draggable: true }).addTo(map);
}

// Evento de clique no botão "Encontrar"
document.getElementById('findButton').addEventListener('click', function () {
  // Obter as coordenadas digitadas nos campos de input
  var lat = parseFloat(document.getElementById('latInput').value);
  var lng = parseFloat(document.getElementById('lngInput').value);

  // Atualizar a posição do marcador
  marker.setLatLng([lat, lng]);
});

// Criar o marcador no mapa
marker = L.marker([-20.4379513, -54.618873], { draggable: true }).addTo(map);

// Evento de arrasto do marcador
document.getElementById('findButton').addEventListener('click', function() {
  // Obter as coordenadas digitadas nos campos de input
  var lat = parseFloat(document.getElementById('latInput').value);
  var lng = parseFloat(document.getElementById('lngInput').value);
  
  // Atualizar a posição do marcador
  marker.setLatLng([lat, lng]);
});

// Criar o marcador no mapa
marker = L.marker([-20.4379513, -54.618873], { draggable: true }).addTo(map);

// Evento de arrasto do marcador
marker.on('dragend', function(event) {
  // Obter a nova posição do marcador
  var latlng = marker.getLatLng();
  var lat = latlng.lat;
  var lng = latlng.lng;
  
  // Atualizar os campos de input com as novas coordenadas
  document.getElementById('latInput').value = lat;
  document.getElementById('lngInput').value = lng;
});

// Camadas base
var baseLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

// Camadas adicionais (overlays)
// configuração do polígono
var myStyle = {
  fillColor: 'rgba(255, 255, 255, 0)', // Cor branca com transparência 0 (totalmente transparente),
  weight: 2,
  opacity: 1,
  color: 'blue',
  fillOpacity: 1
}

var municipios_geojson_dataurl = $("#municipios_geojson").val(); // recupera o valor da URL, onde o id é municipios_geojson
//var municipiosLayer = L.geoJSON([],myStyle).addTo(map);// cria uma camada vazia e adiciona ao mapa

var municipiosLayer = L.geoJSON(null, {
  style: myStyle,// chamando a configuração dos shapefiles
  onEachFeature: function (feature, layer) {
    var popupContent = feature.properties.popup_content;
    layer.bindPopup(popupContent);
  }
}).addTo(map);

$.getJSON(municipios_geojson_dataurl, function (data) {
  municipiosLayer.addData(data);
});
/*
var overlays = {
  "Municipios": municipios,
}

*/


// Adicionar a camada base ao mapa
baseLayer.addTo(map);
