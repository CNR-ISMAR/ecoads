var fixsinglesite = JSON.parse(document.getElementById('fixsinglesite').textContent);


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

var map = L.map('mapsitefix', {
    maxZoom: 14,
    minZoom: 5,
    zoom: 10,
    center:fixsinglesite,
    fullscreenControl: true,
    layers: [baselayer],
    });

var markersite = L.icon({
    iconUrl: '/media/images/Bullseye_7.original.png',
    iconSize: [45, 45],
    popupAnchor: [0, -20],
});

var marker = new L.marker(fixsinglesite, {icon: markersite})
    .addTo(map);