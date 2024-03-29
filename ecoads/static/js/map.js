var watercolor = L.tileLayer('https://stamen-tiles.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
});

var terrain = L.tileLayer('https://stamen-tiles.a.ssl.fastly.net/terrain-background/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
});

var toner = L.tileLayer('https://stamen-tiles.a.ssl.fastly.net/toner-hybrid/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
});

var toner2 = L.tileLayer('https://stamen-tiles.a.ssl.fastly.net/toner-hybrid/{z}/{x}/{y}.png', {
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

var bathymetryLayer2 = L.tileLayer.wms("http://ows.emodnet-bathymetry.eu/wms", {
    layers: 'emodnet:mean_atlas_land',
    format: 'image/png',
    transparent: true,
    attribution: "EMODnet Bathymetry",
    opacity: 0.5
});

var baselayer = L.layerGroup([ watercolor, toner, bathymetryLayer, opensea]);

var baselayer2 = L.layerGroup([terrain, toner2, bathymetryLayer2]);


var map = L.map('map', {
    zoom: 7,
    minZoom: 5,
    // maxZoom: 0,
    fullscreenControl: true,
    center: [43.35, 13.40],
    layers: [baselayer],
});

var baseMaps = {
    "BaseLayer": baselayer,
    "TerrainBaseLayer": baselayer2,
    "osmLayer": osmLayer,
    
};

// var clhoA = L.tileLayer.wms("https://ec.oceanbrowser.net/emodnet/Python/web/wms", {
//     layers: 'Mediterranean Sea/Summer (July-September) - 6-years running averages/Water_body_chlorophyll-a.4Danl.nc*Water_body_chlorophyll-a',
//     format: 'image/png',
//     transparent: true,
//     attribution: "EMODnet Chemistry",
//     opacity: 0.5
// });



var icon_fix_virtual = L.icon({
    iconUrl: '/media/images/Bullseye_7_2.original.png',
    iconSize: [20, 20],
    iconAnchor: [-1, -1],
    popupAnchor: [0, -10],
});

$.getJSON("/djmeasurements/locations/flatjson", function(fixvirtualpoints){
    for (var i = 0; i < fixvirtualpoints.length; i++) {
        //console.log(fixpoints[i].name)
        //console.log(fixpoints[i].latitute)
        //console.log(fixpoints[i].longitude)
        markerfix = new L.marker([fixvirtualpoints[i].latitute, fixvirtualpoints[i].longitude], { icon: icon_fix_virtual })
        .bindPopup(fixvirtualpoints[i].name)
        .addTo(virtualfixlayer);
        //console.log(virtualfixlayer)
    }
    //console.log(virtualfixlayer)
});


virtualfixlayer = L.layerGroup();

var overlayMaps = {
    //"clhorophyll A": clhoA,
    //"Virtual-Point": virtualfixlayer,
};

L.control.layers(baseMaps, overlayMaps).addTo(map);

var baseMaps = {
    "<span style='color: gray'>baselayer</span>": baselayer,
    "osmLayer": osmLayer
};




