import random


class RelojSimulado:

    dias = ["Lunes", "Martes", "Miércoles",
            "Jueves", "Viernes", "Sábado", "Domingo"]

    def __init__(self, hora, minutos):
        self.horas = hora
        self.minutos = minutos

        self.dia = 0
        self.dian = RelojSimulado.dias[0]

    def get_hora(self):
        return f"{self.horas:02d}:{self.minutos:02d}"

    def set_horar(self):
        # Avanzar el tiempo simulado

        tiempoextra = random.randint(6, 13)
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


reloj = RelojSimulado(7, 20)

print(reloj.get_hora())

for num in range(1, 500):

    reloj.set_horar()

    print(reloj.get_hora())
