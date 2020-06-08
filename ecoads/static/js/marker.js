var icon_other_site = L.icon({
    iconUrl: '/media/images/other_site.max-165x165.png',
    iconSize: [15, 15],
    /*iconAnchor: [0, 0],*/
    popupAnchor: [-3, -76],
});
/*L.marker([50.505, 30.57], {icon: myIcon}).addTo(map);*/

var other_ecossites = JSON.parse(document.getElementById('other_ecossites').textContent);
    for (var i = 0; i < other_ecossites.length; i++) {
        marker = new L.marker([other_ecossites[i][1],other_ecossites[i][2]], {icon: icon_other_site})
        .bindPopup(other_ecossites[i][0])
        .addTo(map);
    };

var icon_ecoss_site = L.icon({
    iconUrl: '/media/images/ecoss_site.max-165x165.png',
    iconSize: [45, 45],
    /*iconAnchor: [0, 0],*/
    popupAnchor: [-3, -76],
});

var ecossites = JSON.parse(document.getElementById('ecossites').textContent);
    for (var i = 0; i < ecossites.length; i++) {
        marker = new L.marker([ecossites[i][1],ecossites[i][2]], {icon: icon_ecoss_site})
        .bindPopup(ecossites[i][0])
        .addTo(map);
    };

var polygons = JSON.parse(document.getElementById('polygons').textContent);

var layer = L.geoJSON().addTo(map);
layer.addData(polygons);


/*for (var i = 0; i < polygons.length; i++) {
    poligon = new L.polygon([polygons[i]])
    .bindPopup(polygons[i])
    .addTo(map);
}*/


// questo per aggiungere i poligoni 

/* var polygon = L.polygon([
    [51.509, -0.08],
    [51.503, -0.06],
    [51.51, -0.047]
]).addTo(map); */
