var icon_other_site = L.icon({
    iconUrl: '/media/images/other_site.max-165x165.png',
    iconSize: [15, 15],
    /*iconAnchor: [0, 0],*/
    popupAnchor: [0, -10],
});
/*L.marker([50.505, 30.57], {icon: myIcon}).addTo(map);*/

var other_ecossites = JSON.parse(document.getElementById('other_ecossites').textContent);
for (var i = 0; i < other_ecossites.length; i++) {
    var name = other_ecossites[i][0]
    var link = $(name.link(other_ecossites[i][3])).click(function() {
        //alert("test");
    })[0];
    marker = new L.marker([other_ecossites[i][1], other_ecossites[i][2]], { icon: icon_other_site })
        .bindPopup(link)
        .addTo(map);
};

var icon_ecoss_site = L.icon({
    iconUrl: '/media/images/ecoss_site.max-165x165.png',
    iconSize: [45, 45],
    /*iconAnchor: [0, 0],*/
    popupAnchor: [0, -20],
});

var ecossites = JSON.parse(document.getElementById('ecossites').textContent);
for (var i = 0; i < ecossites.length; i++) {
    var name = ecossites[i][0]
    var link = $(name.link(ecossites[i][3])).click(function() {
        //alert("test");
    })[0];
    marker = new L.marker([ecossites[i][1], ecossites[i][2]], { icon: icon_ecoss_site })
        .bindPopup(link)
        .addTo(map);
};

var stylepolygons = {
    color: "#99c034",
    weight: 1,
    opacity: 0.70

    
};

var polygons = JSON.parse(document.getElementById('polygons').textContent);
var layer = L.geoJSON(polygons, { style: stylepolygons }).addTo(map);
layer.addData(polygons);

var legend = L.control({ position: 'bottomleft' });
legend.onAdd = function(map) {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = ['ECOSS sites', 'Other Sites'];
    labels = ['/media/images/ecoss_site.max-165x165.png', '/media/images/other_site.max-165x165.png'];

    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            (" <img src=" + labels[i] + " height='25' width='25'>") + grades[i] + '<br>';
    }

    return div;

    return div;
};
legend.addTo(map);