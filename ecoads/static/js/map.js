var tonerlite = L.tileLayer('http://tile.stamen.com/toner-lite/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
});

var osmLayer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
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

var baselayer = L.layerGroup([tonerlite, opensea, bathymetryLayer]);

var map = L.map('map', {
    zoom: 7,
    fullscreenControl: true,
    center: [43.50, 13.40],
    layers: [baselayer]
});

var baseMaps = {
    "baselayer": baselayer,
    "osmLayer": osmLayer
};

var clhoA = L.tileLayer.wms("https://ec.oceanbrowser.net/emodnet/Python/web/wms", {
    layers: 'Mediterranean Sea/Summer (July-September) - 6-years running averages/Water_body_chlorophyll-a.4Danl.nc*Water_body_chlorophyll-a',
    format: 'image/png',
    transparent: true,
    attribution: "EMODnet Chemistry",
    opacity: 0.5
});

var overlayMaps = {
    "clhorophyll A": clhoA
};

L.control.layers(baseMaps, overlayMaps).addTo(map);

var baseMaps = {
    "<span style='color: gray'>baselayer</span>": baselayer,
    "osmLayer": osmLayer
};