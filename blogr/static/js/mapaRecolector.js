//crear mapa igual que en recoleccion-de-basura
var mapa = window.map;
var infoWindow = window.infoWindow;

var markers = [];

var marcadorSeleccionado;

function actualizar(lista) {

    //recibe la lista de solicitudes, crea marcadores, limpia los anteriores, añade listener

    //console.log("dentro 1: ", lista);

    //añadir un try

    for (let i = 0; i < markers.length; i++) { //eliminar marcadores anteriores
        markers[i].setMap(null);
    }

    markers = [];

    markers = lista.map((pos) => {
        const latitud = pos.lat;
        const longitud = pos.lng;
        const title = JSON.stringify(pos);
        // desempaquetar ID, STATUS

        const mark = new google.maps.Marker({
            map: mapa,
            position: { lat: latitud, lng: longitud },
            title, //contiene todo el diccionario

        });

        mark.addListener("click", () => {
            //console.log(title);
            infoWindow.setContent(pos.status + ", " + pos.author); //<----------------------cambiar a status
            infoWindow.open(map, mark);

            marcadorSeleccionado = pos;

        });

        return mark;
    });

}

function solicitud() {

    fetch("/rds/solicitudes-del-dia")
        .then((respuesta) => {
            if (!respuesta.ok) {
                throw new Error(`Error en la solicitud: ${respuesta.status}`);
            }
            return respuesta.json();
        })
        .then((lista) => {

            // console.log('Datos obtenidos:', lista);
            actualizar(lista); //crear marcadores con infowindow y listener
        })
        .catch((error) => {
            console.error('Error:', error.message);
        });
}

function actualizarStatus() {
    fetch('/rds/actualizar-status', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(marcadorSeleccionado),
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error al enviar datos:', error);
        });
}

function actualizarMarcadores() {

    //pedir lista de marcadores del día 
    //recibir-solicitudes GET
    //crear un marcador por cada solicitud, con listener e infoWindow
    solicitud();

    //actualizarPosicion()

}

function actualizarPosicion() {
    //imprimir posición actual con marcador personalizado, mapa centrado en la zona, botón, de encuéntrame.

}

document.getElementById('enCamino').addEventListener('click', function () {

    marcadorSeleccionado.status = "En proceso";

    actualizarStatus();
    actualizarMarcadores();
})

document.getElementById('completado').addEventListener('click', function () {

    marcadorSeleccionado.status = "Solicitud completada";
    actualizarStatus();
    actualizarMarcadores();
})

document.getElementById('errorAlCompletar').addEventListener('click', function () {

    marcadorSeleccionado.status = "No pude completar tu solicitud";
    actualizarStatus();
    actualizarMarcadores();
})

actualizarMarcadores();