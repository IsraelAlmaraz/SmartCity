function initMap() {

    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: { lat: 19.034, lng: -98.2 },
        // styles: [//general de Calles ,texto
        //     { elementType: "geometry", stylers: [{ color: "#000000" }] },
        //     { elementType: "labels.text.stroke", stylers: [{ color: "#242f3e" }] },
        //     { elementType: "labels.text.fill", stylers: [{ color: "#746855" }] },
        //     {
        //       featureType: "administrative.locality",
        //       elementType: "labels.text.fill",
        //       stylers: [{ color: "#d59563" }],
        //     },
        //     {// Textos de mercados ,escuelas etc.
        //       featureType: "poi",
        //       elementType: "labels.text.fill",
        //       stylers: [{ color: "#ffffff" }],
        //     },
        //     {//Rellenos Parques y Centros Historicos
        //       featureType: "poi.park",
        //       elementType: "geometry",
        //       stylers: [{ color: "#263c3f" }],
        //     },
        //     {//texto  parques
        //       featureType: "poi.park",
        //       elementType: "labels.text.fill",
        //       stylers: [{ color: "#6b9a76" }],
        //     },
        //     { // Calles
        //       featureType: "road",
        //       elementType: "geometry",
        //       stylers: [{ color: "#38414e" }],
        //     },
        //     {//Calles contorno exterior
        //       featureType: "road",
        //       elementType: "geometry.stroke",
        //       stylers: [{ color: "#212a37" }],
        //     },
        //     {
        //       featureType: "road",
        //       elementType: "labels.text.fill",
        //       stylers: [{ color: "#9ca5b3" }],
        //     },
        //     {
        //       featureType: "road.highway",
        //       elementType: "geometry",
        //       stylers: [{ color: "#746855" }],
        //     },
        //     {
        //       featureType: "road.highway",
        //       elementType: "geometry.stroke",
        //       stylers: [{ color: "#1f2835" }],
        //     },
        //     {
        //       featureType: "road.highway",
        //       elementType: "labels.text.fill",
        //       stylers: [{ color: "#f3d19c" }],
        //     },
        //     {
        //       featureType: "transit",
        //       elementType: "geometry",
        //       stylers: [{ color: "#2f3948" }],
        //     },
        //     {
        //       featureType: "transit.station",
        //       elementType: "labels.text.fill",
        //       stylers: [{ color: "#d59563" }],
        //     },
        //     {
        //       featureType: "water",
        //       elementType: "geometry",
        //       stylers: [{ color: "#17263c" }],
        //     },
        //     {
        //       featureType: "water",
        //       elementType: "labels.text.fill",
        //       stylers: [{ color: "#515c6d" }],
        //     },
        //     {
        //       featureType: "water",
        //       elementType: "labels.text.stroke",
        //       stylers: [{ color: "#17263c" }],
        //     },
        //   ],
        
    });


    var recorrido = [
        { lat: 18.982259, lng: -98.217176 },
        { lat: 18.982117, lng: -98.21775 },
        { lat: 18.982899, lng: -98.217474 },
        { lat: 18.983903, lng: -98.217206 },
        { lat: 18.984867, lng: -98.217077 },
        { lat: 18.985357, lng: -98.216986 },
        { lat: 18.987239, lng: -98.215715 },
        { lat: 18.988136, lng: -98.215147 },
        { lat: 18.99018, lng: -98.214439 },
        { lat: 18.99247, lng: -98.213399 },
        { lat: 18.993763, lng: -98.21311 },
        { lat: 18.995046, lng: -98.211699 },
        { lat: 19.003928, lng: -98.207107 },
        { lat: 19.004384, lng: -98.207005 },
        { lat: 19.005749, lng: -98.204763 },
        { lat: 19.006078, lng: -98.204564 },
        { lat: 19.007737, lng: -98.204033 },
        { lat: 19.013312, lng: -98.202317 },
        { lat: 19.016953, lng: -98.201212 },
        { lat: 19.02025, lng: -98.199496 },
        { lat: 19.026736, lng: -98.200978 },
        { lat: 19.030057, lng: -98.201809 },
        { lat: 19.030149, lng: -98.201753 },
        { lat: 19.030194, lng: -98.201512 },
        { lat: 19.030374, lng: -98.201254 },
        { lat: 19.030597, lng: -98.201211 },
        { lat: 19.030818, lng: -98.201306 },
        { lat: 19.030975, lng: -98.201491 },
        { lat: 19.030993, lng: -98.201714 },
        { lat: 19.030922, lng: -98.201923 },
        { lat: 19.030853, lng: -98.202004 },
        { lat: 19.039386, lng: -98.2185 },
        { lat: 19.04176, lng: -98.223279 },
        { lat: 19.041764, lng: -98.223341 },
        { lat: 19.035425, lng: -98.226945 },
        { lat: 19.033304, lng: -98.228275 },
        { lat: 19.032548, lng: -98.228613 },
        { lat: 19.031686, lng: -98.229042 },
        { lat: 19.030936, lng: -98.229622 },
        { lat: 19.030221, lng: -98.230544 },
        { lat: 19.029597, lng: -98.231537 },
        { lat: 19.029029, lng: -98.232416 },
        { lat: 18.982259, lng: -98.217176 },

    ];

    for (var i = 0; i < recorrido.length - 2; i++) {
        var linea = new google.maps.Polyline({
            path: [recorrido[i], recorrido[i + 1]],
            geodesic: true,
            strokeColor: '#0000FF',
            strokeOpacity: 1.0,
            strokeWeight: 5
        });
        linea.setMap(map);
    }

    return map;
}

window.initMap = initMap;