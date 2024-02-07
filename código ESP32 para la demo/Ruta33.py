import urequests
import utime
import simuladorV2
# import ujson

# Configura tu red WiFi
ssid = "ISRA-CASA-HOUSE-2.4G"
password = "holaholahola"

# mi 11 lite 5g
# ssid = "isra"
# password = "holahola"

# casa de Mays
# ssid = "INFINITUME29A_2.4"
# password = "xqBkTx8Hgz"

# url = "https://isra779.pythonanywhere.com/obtenerlista"
# url = "http://192.168.100.3:5000/posiciones"

# mi 11 lite 5g
url = "http://192.168.98.163:5000/posiciones"
url = "http://192.168.100.3:5000/mtp/posiciones"

# casa de Mays
# url = "http://192.168.1.105:5000/posiciones"


def conectar_wifi():
    import network

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando a WiFi...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print("Conectado a WiFi:", wlan.ifconfig())


def enviar_datos(datos):
    response = urequests.post(url, json=datos)
    # print(response.text)
    if response.status_code == 200:
        print("Datos enviados correctamente.")

    else:
        print("Error al enviar datos. Código de estado:", response.status_code)
    response.close()

def guardar_datos(datos):
    link = "http://192.168.100.3:5000/mtp/guardar-datos"
    response = urequests.post(link, json=datos)
    # print(response.text)
    if response.status_code == 200:
        print("Datos enviados correctamente.")

    else:
        print("Error al enviar datos. Código de estado:", response.status_code)
    response.close()


# Conexión a WiFi
conectar_wifi()

U1 = simuladorV2.Camion("Ruta 33 U1", 1, 7, 0)
U2 = simuladorV2.Camion("Ruta 33 U2", 8, 7, 15)
U3 = simuladorV2.Camion("Ruta 33 U3", 20, 7, 40)
U4 = simuladorV2.Camion("Ruta 33 U4", 26, 8, 0)

lista_de_camiones = [U1, U2, U3, U4]

while True:
    cont = 0

    while cont <= 7:
        lista = simuladorV2.circular(lista_de_camiones)  # todos los carros avanzan

        for dicc in lista:
            enviar_datos(dicc)
            utime.sleep_ms(100)

        cont += 1

    for camion in lista_de_camiones:
        guardar_datos(camion.get_dicc())



