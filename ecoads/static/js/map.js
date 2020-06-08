var map = L.map('map', {
    zoom: 7,
    fullscreenControl: true,
    center: [44.00, 13.00]
    });

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


