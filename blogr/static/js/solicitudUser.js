var zona1 = window.zona1;
var map = window.map;

const fechaInput = document.getElementById('fecha');
const textbox = document.getElementById('miCuadroDeTexto');

//hacer get para status

console.log(zona1.getPath().getArray());

var marcador; var coordenadas; var area;

function agregarMarcador(evento) {
    if (marcador) {
        marcador.setMap(null);
    }

    area = 1;

    marcador = new google.maps.Marker({
        position: evento.latLng,
        map: map,
        draggable: false
    });

    coordenadas = [marcador.getPosition().lat(), marcador.getPosition().lng()]


    console.log(coordenadas);
}

google.maps.event.addListener(zona1, 'click', agregarMarcador);

fechaInput.addEventListener('change', function () {
    const fechaSeleccionada = fechaInput.value;
    console.log('Fecha seleccionada:', fechaSeleccionada);
    console.log(typeof fechaInput.value)
});


document.getElementById('BotonEnviar').addEventListener('click', function () {

    const fecha = fechaInput.value;
    const alias = textbox.value;
    const solicitud = {};

    if (coordenadas === undefined) {
        alert('Aún no has especificado un punto de recogida.');
    }

    else if (fecha === "") {
        alert('Aún no has especificado una fecha.');
    }

    else {
        alert('¡Solicitud aprobada!, pasaremos por tu basura el ' + fecha);

        // Agregar elementos al diccionario
        solicitud['lat'] = coordenadas[0];
        solicitud['lng'] = coordenadas[1];
        solicitud['area'] = area;
        solicitud['fecha'] = fecha;
        // solicitud['status'] = "Aceptado";
        solicitud['alias'] = alias;

        fetch('/rds/guardar-datos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(solicitud),
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.error('Error al enviar datos:', error);
            });
    }



});

//botón enviar, al presionar mandar 'coordenadas' a la base de datos