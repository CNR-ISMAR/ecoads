var map = L.map('map', {
    zoom: 7,
    fullscreenControl: true,
    center: [44.00, 13.00]
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


/*var inspireWgs84Grid = function(levels, prefix) {
    var projection = ol.proj.get('EPSG:4326');

    var projectionExtent = projection.getExtent();
    var resolution = ol.extent.getWidth(projectionExtent) / 512;
    
    var resolutions = new Array(levels);
    var matrixIds = new Array(levels);
    
    for (var z = 0; z < levels; z++) {
        resolutions[z] = resolution / Math.pow(2, z);
        matrixIds[z] = z;
    }
    
    return new ol.tilegrid.WMTS({
        origin: ol.extent.getTopLeft(projectionExtent),
        resolutions: resolutions,
        matrixIds: matrixIds
    });				
}

var layer = new ol.layer.Tile({
    extent: [-36, 25, 43, 85],
    source : new ol.source.WMTS({
        url : 'https://tiles.emodnet-bathymetry.eu/2020/baselayer/{TileMatrixSet}/{TileMatrix}/{TileCol}/{TileRow}.png',
        layer : 'baselayer',
        requestEncoding : 'REST',
        matrixSet : 'inspire_quad',
        format : 'image/png',
        projection : "EPGS:4326",
        tileGrid : inspireWgs84Grid(12, '')
    })
});


var map = new ol.Map({
	layers: [ layer ],
	target: 'map',
	controls: ol.control.defaults(),
	view: new ol.View({	
		projection: 'EPSG:4326',
		center: [5, 47],
		zoom: 5
	})	
}); */