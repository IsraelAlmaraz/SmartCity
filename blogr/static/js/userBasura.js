function initMap() {

    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: { lat: 19.040589, lng: -98.198803 },
    });

    var poligono = new google.maps.Polygon({
        paths: [
            { lat: 19.025236, lng: -98.190778 },
            { lat: 19.039443, lng: -98.218553 },
            { lat: 19.058215, lng: -98.208309 },
            { lat: 19.043736, lng: -98.180527 }
        ],
        strokeColor: '#FFFF00', // Color del borde del polígono
        strokeOpacity: 0.8, // Opacidad del borde
        strokeWeight: 2, // Grosor del borde
        fillColor: '#FFFF00', // Color de relleno del polígono
        fillOpacity: 0.2 // Opacidad del relleno
    });

    poligono.setMap(map);

    window.zona1 = poligono;
    window.map = map;

    //return map;
}

window.initMap = initMap;