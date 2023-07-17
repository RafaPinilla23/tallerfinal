import time

class Vehiculo:
    def __init__(self, id_vehiculo, velocidad, posicion):
        self.id_vehiculo = id_vehiculo
        self.velocidad = velocidad
        self.posicion = posicion
        self.posicioninicial = posicion
        self.distanciar = 0

    #MetodoNuevo
    def caldistancia(self):
        self.distanciar = self.posicion - self.posicioninicial
        print(f"{self.distanciar}, distancia recorrida respectivamente")
    
    def avanzar(self):
        self.posicion += self.velocidad

    def mostrar_estado(self):
        print(f"Vehículo {self.id_vehiculo}: Posición = {self.posicion}, Velocidad = {self.velocidad}")

class Semaforo:
    def __init__(self, nsemaforo, estado):
        self.nsemaforo = nsemaforo
        self.estado = estado  

    def cambiar_estado(self):
        self.estado = not self.estado

    def mostrar_estado(self):
        estado_str = "Verde" if self.estado else "Rojo"
        print(f"Semaforo {self.nsemaforo}: Estado = {estado_str}")

class Cruce(Semaforo):
    def __init__(self, ncruce, semaforos):
        self.ncruce = ncruce
        self.semaforos = semaforos

    def obtener_semaforo(self, nsemaforo):
        return self.semaforos[nsemaforo]

    def simular(self, duracion, vehiculos):
        for segundo in range(duracion):
            print(f"Segundo {segundo + 1}:")
            for vehiculo in vehiculos:
                vehiculo.avanzar()
                vehiculo.mostrar_estado()

            for semaforo in self.semaforos:
                semaforo.cambiar_estado()
                semaforo.mostrar_estado()

            time.sleep(1)
        for vehiculo in vehiculos:
            vehiculo.caldistancia()

vehiculo1 = Vehiculo(1, 3, 3)
vehiculo2 = Vehiculo(2, 4, 5)

semaforo1 = Semaforo(1, True)  
semaforo2 = Semaforo(2, False)  

cruce1 = Cruce(1, [semaforo1, semaforo2])

tiempo = int(input("Ingrese el tiempo en segundos para la simulacion: "))
cruce1.simular(tiempo, [vehiculo1, vehiculo2])
