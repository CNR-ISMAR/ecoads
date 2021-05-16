// Sites imported from DEIMS sdr but NOT case studies in ECOSS Project
var icon_other_site = L.icon({
    iconUrl: '/media/images/Certificate_7_1.original.png',
    iconSize: [20, 20],
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

// Sites imported fromm DEIMS sdr AND case studies in ECOSS Project
var icon_ecoss_site = L.icon({
    iconUrl: '/media/images/Certificate_7.original.png',
    iconSize: [30, 30],
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

// Geometry for ECOSS Case studies sites
var stylepolygons = {
    color: "#1b9e77",
    weight: 1,
    opacity: 0.70
};

var polygons = JSON.parse(document.getElementById('polygons').textContent);
var layer = L.geoJSON(polygons, { style: stylepolygons }).addTo(map);
layer.addData(polygons);

// LEGEND
var legend = L.control({ position: 'bottomleft' });
legend.onAdd = function(map) {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = ['ECOAdS sites', 'Other LTER Sites', 'Fixed-Point Observing Systems'];
    labels = ['/media/images/Certificate_7.original.png', '/media/images/Certificate_7_1.original.png', '/media/images/Bullseye_7.original.png'];

    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            (" <img src=" + labels[i] + " height='25' width='25'>") + grades[i] + '<br>';
    }

    return div;

    return div;
};
legend.addTo(map);


var fix_point_icon = L.icon({
    iconUrl: '/media/images/Bullseye_7.original.png',
    iconSize: [20, 20],
    iconAnchor: [-1, -1],
    popupAnchor: [0, -10],
});
/*L.marker([50.505, 30.57], {icon: myIcon}).addTo(map);*/

var fix_point = JSON.parse(document.getElementById('fix_point').textContent);
for (var i = 0; i < fix_point.length; i++) {
    var name = fix_point[i][0]
    var link = $(name.link("fix/" + fix_point[i][3])).click(function() {
        //alert("test");
    })[0];
    //console.log(other_ecossites)
    marker = new L.marker([fix_point[i][1], fix_point[i][2]], { icon: fix_point_icon })
    
        .bindPopup(link)
        .addTo(map);
};