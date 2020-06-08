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



