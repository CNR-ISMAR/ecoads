var singlesite = JSON.parse(document.getElementById('singlesite').textContent);
var polygon = JSON.parse(document.getElementById('polygon').textContent);

var map = L.map('mapsite', {
maxZoom: 14,
minZoom: 5,
zoom: 10,
center:singlesite,
fullscreenControl: true,
});

L.tileLayer('http://tile.stamen.com/toner-lite/{z}/{x}/{y}.png', {
attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
}).addTo(map);

L.tileLayer('http://tiles.openseamap.org/seamark/{z}/{x}/{y}.png', {
attribution: ''
}).addTo(map);

var bathymetryLayer = L.tileLayer.wms("http://ows.emodnet-bathymetry.eu/wms", {
        layers: 'emodnet:mean_atlas_land',
        format: 'image/png',
        transparent: true,
        attribution: "EMODnet Bathymetry",
        opacity: 0.5
    }).addTo(map);

var markersite = L.icon({
    iconUrl: '/media/images/Certificate_7.original.png',
    iconSize: [45, 45],
    popupAnchor: [0, -20],
});

var denomination = JSON.parse(document.getElementById('denomination').textContent); 

var marker = new L.marker(singlesite, {icon: markersite})
        .bindPopup(denomination)
        .addTo(map);

var stylepolygons = {
color: "#1b9e77",
weight: 1,
opacity: 0.20
};

if (polygon!="") {
    var layer = L.geoJSON(polygon, {style: stylepolygons}).addTo(map);
    layer.addData(polygon);
    map.fitBounds(layer.getBounds(),{maxZoom : 10});
};

  // aggiungere json

var icon_fix = L.icon({
    iconUrl: '/media/images/fix_2.0.original.png',
    iconSize: [20, 20],
    iconAnchor: [-1, -1],
    popupAnchor: [0, -10],
});

$.getJSON("/djmeasurements/locations/flatjson", function(fixpoints){
    for (var i = 0; i < fixpoints.length; i++) {

        //console.log(fixpoints[i].name)
        //console.log(fixpoints[i].latitute)
        //console.log(fixpoints[i].longitude)
        markerfix = new L.marker([fixpoints[i].latitute, fixpoints[i].longitude], { icon: icon_fix })
        .bindPopup(fixpoints[i].name)
        .addTo(map);
    }
});  

// LEGEND
var legend = L.control({ position: 'bottomright' });
legend.onAdd = function(map) {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = ['Fixed-Point Observing Systems'];
    labels = ['/media/images/fix_2.0.original.png'];

    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            (" <img src=" + labels[i] + " height='20' width='20'>") + grades[i] + '<br>';
    }

    return div;

};
legend.addTo(map);