    var singlesite = JSON.parse(document.getElementById('singlesite').textContent);
    var polygon = JSON.parse(document.getElementById('polygon').textContent);
    
    var map = L.map('mapsite', {
    maxZoom: 14,
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
        iconUrl: '/media/images/markersite.max-165x165.png',
        iconSize: [45, 45],
        popupAnchor: [0, -20],
    });

    var denomination = JSON.parse(document.getElementById('denomination').textContent); 
    
    var marker = new L.marker(singlesite, {icon: markersite})
            .bindPopup(denomination)
            .addTo(map);

    var stylepolygons = {
    color: "#590416",
    weight: 1,
    opacity: 0.20
    };
    
    if (polygon!="") {
        var layer = L.geoJSON(polygon, {style: stylepolygons}).addTo(map);
        layer.addData(polygon);
        map.fitBounds(layer.getBounds(),{maxZoom : 10});
    };