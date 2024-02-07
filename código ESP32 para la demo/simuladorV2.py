""" Librería que permite simular el avance de camiones que
se mueven sobre líneas en específico """

import random


class RelojSimulado:

    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def __init__(self, hora, minutos):
        self.horas = hora
        self.minutos = minutos

        self.dia = 0
        self.dian = RelojSimulado.dias[0]

    def get_hora(self):
        return f"{self.horas:02d}:{self.minutos:02d}"

    def set_horar(self):
        # Avanzar el tiempo simulado

        tiempoextra = random.randint(4, 9)
        cambiarhora = (self.minutos + tiempoextra) / 60

        resetearh = (self.horas + 1) / 22

        if cambiarhora >= 1:

            if resetearh >= 1:
                self.horas = 7

                self.dia = (self.dia + 1) % 7
                self.dian = RelojSimulado.dias[self.dia]
            else:
                self.horas += 1
        self.minutos = (self.minutos + tiempoextra) % 60


class Line:
    "obtiene la ecuación de la recta y calcula el siguiente punto del recorrido"

    def __init__(self, num, piy, pix, pfy, pfx):
        """Lat es coordenada en y, Lng es coordenada en x"""
        self.num = num
        self.pix = pix
        self.piy = piy

        self.pfx = pfx
        self.pfy = pfy

        self.m = (pfy - piy) / (pfx - pix)

        self.b = pfy - self.m * pfx

        if pix > pfx:
            self.positive = False
            self.rango = [pfx, pix]
        else:
            self.positive = True
            self.rango = [pix, pfx]

        print(self.pix, self.piy)

    def mandar_al_inicio(self):
        "Devuelve las coordenadas iniciales de la línea"
        return [self.piy, self.pix]

    def avanzar(self, px):
        "recorre en pasos discretos el rango [pix, pfx] y devuelve la f(px) = py"
        if self.positive is True:
            return self.aumentar(px)

        else:
            return self.decrementar(px)

    def aumentar(self, px):
        "componente en x del vector desplazamiento es positivo"
        new_px = px + 0.001

        if self.pix <= new_px <= self.pfx:
            new_py = round(self.m * new_px + self.b, 5)
            return [new_py, new_px]

        return self.num + 1

    def decrementar(self, px):
        "componente en x del vector desplazamiento es negativo"
        new_px = px - 0.001

        if self.pfx <= new_px <= self.pix:
            new_py = round(self.m * new_px + self.b, 5)
            return [new_py, new_px]

        return self.num + 1


class Camion:
    "Camión, tiene latm lng, línea, id, tiene método de avanzar"
    hora = "07:00:00"
    lista_de_lineas = [
        Line(0, 18.982259, -98.217176, 18.982117, -98.21775),
        Line(1, 18.982117, -98.21775, 18.982899, -98.217474),
        Line(2, 18.982899, -98.217474, 18.983903, -98.217206),
        Line(3, 18.983903, -98.217206, 18.984867, -98.217077),
        Line(4, 18.984867, -98.217077, 18.985357, -98.216986),
        Line(5, 18.985357, -98.216986, 18.987239, -98.215715),
        Line(6, 18.987239, -98.215715, 18.988136, -98.215147),
        Line(7, 18.988136, -98.215147, 18.99018, -98.214439),
        Line(8, 18.99018, -98.214439, 18.99247, -98.213399),
        Line(9, 18.99247, -98.213399, 18.993763, -98.21311),
        Line(10, 18.993763, -98.21311, 18.995046, -98.211699),
        Line(11, 18.995046, -98.211699, 19.003928, -98.207107),
        Line(12, 19.003928, -98.207107, 19.004384, -98.207005),
        Line(13, 19.004384, -98.207005, 19.005749, -98.204763),
        Line(14, 19.005749, -98.204763, 19.006078, -98.204564),
        Line(15, 19.006078, -98.204564, 19.007737, -98.204033),
        Line(16, 19.007737, -98.204033, 19.013312, -98.202317),
        Line(17, 19.013312, -98.202317, 19.016953, -98.201212),
        Line(18, 19.016953, -98.201212, 19.02025, -98.199496),
        Line(19, 19.02025, -98.199496, 19.026736, -98.200978),
        Line(20, 19.026736, -98.200978, 19.030057, -98.201809),
        Line(21, 19.030057, -98.201809, 19.030149, -98.201753),
        Line(22, 19.030149, -98.201753, 19.030194, -98.201512),
        Line(23, 19.030194, -98.201512, 19.030374, -98.201254),
        Line(24, 19.030374, -98.201254, 19.030597, -98.201211),
        Line(25, 19.030597, -98.201211, 19.030818, -98.201306),
        Line(26, 19.030818, -98.201306, 19.030975, -98.201491),
        Line(27, 19.030975, -98.201491, 19.030993, -98.201714),
        Line(28, 19.030993, -98.201714, 19.030922, -98.201923),
        Line(29, 19.030922, -98.201923, 19.030853, -98.202004),
        Line(30, 19.030853, -98.202004, 19.039386, -98.2185),
        Line(31, 19.039386, -98.2185, 19.04176, -98.223279),
        Line(32, 19.04176, -98.223279, 19.041764, -98.223341),
        Line(33, 19.041764, -98.223341, 19.035425, -98.226945),
        Line(34, 19.035425, -98.226945, 19.033304, -98.228275),
        Line(35, 19.033304, -98.228275, 19.032548, -98.228613),
        Line(36, 19.032548, -98.228613, 19.031686, -98.229042),
        Line(37, 19.031686, -98.229042, 19.030936, -98.229622),
        Line(38, 19.030936, -98.229622, 19.030221, -98.230544),
        Line(39, 19.030221, -98.230544, 19.029597, -98.231537),
        Line(40, 19.029597, -98.231537, 19.029029, -98.232416),
    ]

    def __init__(self, iden, num_linea, hora, minutos):
        "linea: entero que va de 0 a lista_de_lineas.length()"
        self.iden = iden
        self.linea = Camion.lista_de_lineas[num_linea]  # objeto Line actual

        # mandar al inicio de Line actual
        self.lat, self.lng = self.linea.mandar_al_inicio()

        self.lleno = False
        self.reloj_interno = RelojSimulado(hora, minutos)

        self.estado = 1

    def avanzar(self):
        "Avanza sobre la línea actual"

        try:
            self.lat, self.lng = self.linea.avanzar(self.lng)
            return self.get_dicc()

        except TypeError:
            sig_num = self.linea.avanzar(self.lng) % len(Camion.lista_de_lineas)

            if sig_num in (7, 13, 19, 25, 30, 39):
                self.reloj_interno.set_horar()
                self.estado = (self.estado % 3) + 1

            self.linea = Camion.lista_de_lineas[sig_num]

            self.lat, self.lng = self.linea.mandar_al_inicio()
            return self.get_dicc()

    def get_dicc(self):
        "Devuelve el diccionario que se enviará a al mapa"
        hora = self.reloj_interno.get_hora()
        dia = self.reloj_interno.dian

        dicc = {
            "id": self.iden,
            "lat": self.lat,
            "lon": self.lng,
            "hora": hora,
            "dia": dia,
            "estado": self.estado
        }
        return dicc


def circular(camiones):
    "Hace avanzar a todos los camiones, almacena sus diccionarios en una lista"
    diccionarios = []

    for cam in camiones:
        diccionarios.append(cam.avanzar())

    return diccionarios
