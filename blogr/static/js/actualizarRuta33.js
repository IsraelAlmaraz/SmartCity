var mapa = window.initMap();

var markers = [];

var icon = { //amarillo
    url: "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Icon-mode-bus-default.svg/2048px-Icon-mode-bus-default.svg.png",
    size: new google.maps.Size(50, 50),
    scaledSize: new google.maps.Size(25, 25), // Tamaño en pantalla

    anchor: new google.maps.Point(12.5, 12.5)
};

function actualizar(lista) {

    console.log("dentro 1: ", lista);

    for (let i = 0; i < markers.length; i++) {
        markers[i].setMap(null);
    }

    markers = [];

    markers = lista.map((pos) => {
        let latitud = pos.lat;
        let longitud = pos.lon;


        const mark = new google.maps.Marker({
            map: mapa,
            position: { lat: latitud, lng: longitud },
            icon: icon,

        });


        return mark;
    });

}

function solicitud() {

    fetch("/mtp/posiciones")
        .then((respuesta) => {
            if (!respuesta.ok) {
                throw new Error(`Error en la solicitud: ${respuesta.status}`);
            }
            return respuesta.json();
        })
        .then((lista) => {

            console.log('Datos obtenidos:', lista);
            actualizar(lista);
        })
        .catch((error) => {
            console.error('Error:', error.message);
        });
}

solicitud();
setInterval(solicitud, 3000);