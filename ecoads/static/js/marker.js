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
    var link = $(name.link("site/" + other_ecossites[i][3])).click(function() {
        //alert("test");
    })[0];
    //console.log(other_ecossites)
    marker = new L.marker([other_ecossites[i][1], other_ecossites[i][2]], { icon: icon_other_site })
    
        .bindPopup(link)
        .addTo(map);
};

var icon_ecoss_site = L.icon({
    iconUrl: '/media/images/ecoss_site.max-165x165.png',
    iconSize: [40, 40],
    /*iconAnchor: [0, 0],*/
    popupAnchor: [0, -20],
});

var ecossites = JSON.parse(document.getElementById('ecossites').textContent);
for (var i = 0; i < ecossites.length; i++) {
    var name = ecossites[i][0]
    var link = $(name.link("site/" + ecossites[i][3])).click(function() {
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
        grades = ['ECOAdS sites', 'Other Sites', 'Fixed-Point Observing Systems'];
    labels = ['/media/images/ecoss_site.max-165x165.png', '/media/images/other_site.max-165x165.png', '/media/images/fix_2.0_qGnWXr1.original.png'];

    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            (" <img src=" + labels[i] + " height='25' width='25'>") + grades[i] + '<br>';
    }

    return div;

    return div;
};
legend.addTo(map);


// aggiungere json

var icon_fix = L.icon({
    iconUrl: '/media/images/fix_2.0_qGnWXr1.original.png',
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

