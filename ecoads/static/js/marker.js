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

// Sites imported fromm DEIMS sdr AND case studies in ECOSS Project LTER
var icon_ecoss_site_lter = L.icon({
    iconUrl: '/media/images/Certificate_7.original.png',
    iconSize: [30, 30],
    /*iconAnchor: [0, 0],*/
    popupAnchor: [0, -20],
});

var ltersites = JSON.parse(document.getElementById('ltersites').textContent);
for (var i = 0; i < ltersites.length; i++) {
    var name = ltersites[i][0]
    var link = $(name.link("site/" + ltersites[i][3])).click(function() {
        //alert("test");
    })[0];
    marker = new L.marker([ltersites[i][1], ltersites[i][2]], { icon: icon_ecoss_site_lter })
        .bindPopup(link)
        .addTo(map);
};

// Sites imported fromm DEIMS sdr AND case studies in ECOSS Project N2K
var icon_ecoss_site_n2k = L.icon({
    iconUrl: '/media/images/Certificate_71.original.png',
    iconSize: [30, 30],
    /*iconAnchor: [0, 0],*/
    popupAnchor: [0, -20],
});

var n2ksites = JSON.parse(document.getElementById('n2ksites').textContent);
for (var i = 0; i < n2ksites.length; i++) {
    var name = n2ksites[i][0]
    var link = $(name.link("site/" + n2ksites[i][3])).click(function() {
        //alert("test");
    })[0];
    marker = new L.marker([n2ksites[i][1], n2ksites[i][2]], { icon: icon_ecoss_site_n2k })
        .bindPopup(link)
        .addTo(map);
};

// var ecossites = JSON.parse(document.getElementById('ecossites').textContent);
// for (var i = 0; i < ecossites.length; i++) {
//     var name = ecossites[i][0]
//     var link = $(name.link("site/" + ecossites[i][3])).click(function() {
//         //alert("test");
//     })[0];
//     marker = new L.marker([ecossites[i][1], ecossites[i][2]], { icon: icon_ecoss_site })
//         .bindPopup(link)
//         .addTo(map);
// };

// Geometry for ECOSS Case studies sites
var stylepolygons_lter = {
    color: "#1b9e77",
    weight: 1,
    opacity: 0.70
};

var stylepolygons_n2k = {
    color: "#66a61e",
    weight: 1,
    opacity: 0.70
};

var polygons_lter = JSON.parse(document.getElementById('polygons_lter').textContent);
var layer = L.geoJSON(polygons_lter, { style: stylepolygons_lter }).addTo(map);
layer.addData(polygons_lter);

var polygons_n2k = JSON.parse(document.getElementById('polygons_n2k').textContent);
var layer_n2k = L.geoJSON(polygons_n2k, { style: stylepolygons_n2k }).addTo(map);
layer_n2k.addData(polygons_n2k);

// LEGEND
var legend = L.control({ position: 'bottomleft' });
legend.onAdd = function(map) {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = [ ' ECOAdS Natura 2000 sites', ' ECOAdS LTER sites', ' Other LTER Sites', ' Fixed-Point Observing Systems'];
    labels = ['/media/images/Certificate_71.original.png', '/media/images/Certificate_7.original.png', '/media/images/Certificate_7_1.original.png', '/media/images/Bullseye_7.original.png'];

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