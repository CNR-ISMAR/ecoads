var singlesite = JSON.parse(document.getElementById('singlesite').textContent);
var polygon = JSON.parse(document.getElementById('polygon').textContent);





var toner = L.tileLayer('https://stamen-tiles.a.ssl.fastly.net/toner-hybrid/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
});

var watercolor = L.tileLayer('https://stamen-tiles.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
});

var opensea = L.tileLayer('http://tiles.openseamap.org/seamark/{z}/{x}/{y}.png', {
    attribution: ''
});

var bathymetryLayer = L.tileLayer.wms("http://ows.emodnet-bathymetry.eu/wms", {
        layers: 'emodnet:mean_atlas_land',
        format: 'image/png',
        transparent: true,
        attribution: "EMODnet Bathymetry",
        opacity: 0.5
    });



var baselayer = L.layerGroup([ watercolor, toner, bathymetryLayer, opensea])


var map = L.map('mapsite', {
    maxZoom: 14,
    minZoom: 5,
    zoom: 10,
    center:singlesite,
    fullscreenControl: true,
    layers: [baselayer]
    });


var n2k = JSON.parse(document.getElementById('n2k').textContent);

if (n2k == false) {
    var markersite = L.icon({
        iconUrl: '/media/images/Certificate_7.original.png',
        iconSize: [45, 45],
        popupAnchor: [0, -20],
    });

    var stylepolygons = {
        color: "#1b9e77",
        weight: 1,
        opacity: 0.20
        };
        
};

if (n2k == true) {
    var markersite = L.icon({
        iconUrl: '/media/images/Certificate_71.original.png',
        iconSize: [45, 45],
        popupAnchor: [0, -20],
    });

    var stylepolygons = {
        color: "#66a61e",
        weight: 1,
        opacity: 0.20
        };
    
};


var denomination = JSON.parse(document.getElementById('denomination').textContent); 



var marker = new L.marker(singlesite, {icon: markersite})
        .bindPopup(denomination)
        .addTo(map);


if (polygon!="") {
    var layer = L.geoJSON(polygon, {style: stylepolygons}).addTo(map);
    layer.addData(polygon);
    map.fitBounds(layer.getBounds(),{maxZoom : 10});
};

  // aggiungere json

var icon_fix = L.icon({
    iconUrl: '/media/images/Bullseye_7.original.png',
    iconSize: [25, 25],
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
    labels = ['/media/images/Bullseye_7.original.png'];

    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            (" <img src=" + labels[i] + " height='20' width='20'>") + grades[i] + '<br>';
    }

    return div;

};
legend.addTo(map);