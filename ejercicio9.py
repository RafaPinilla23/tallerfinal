class Evento:
    def __init__(self, nombre, fecha, hora, ubicacion):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.ubicacion = ubicacion
        self.participantes = []

    def registrar_participante(self, participante):
        self.participantes.append(participante)

    def enviar_notificacion(self, mensaje):
        for participante in self.participantes:
            notificacion = Notificacion(mensaje, participante)
            notificacion.enviar()
    
    #MetodoNuevo
    def mostrar_participantes(self):
        print("")
        for participante in self.participantes:
            print(participante.nombre)

    def gestionar_logistica(self):
        print("\nGestionando logística para el evento", self.nombre)
        print("Reservando lugar en", self.ubicacion)
        print("Contratando servicios de catering")
        print("Preparando equipo de sonido y proyección")

class Participante(Evento):
    def __init__(self, nombre, correo_electronico, telefono):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.telefono = telefono

class Notificacion:
    def __init__(self, mensaje, destinatario):
        self.mensaje = mensaje
        self.destinatario = destinatario

    def enviar(self):
        print("\nEnviando notificación a", self.destinatario.nombre, "al correo", self.destinatario.correo_electronico, "con el mensaje:", self.mensaje)

#Creando un evento
evento = Evento("Stream Fighters", "15/8/2023", "10:00", "Movistar Arena")

#Registrando participantes
participante1 = Participante("Julian Pérez", "juliperez02@gmail.com", "3147854125")
participante2 = Participante("María Salcedo", "maria.salceg@gmail.com", "3048852189")
evento.registrar_participante(participante1)
evento.registrar_participante(participante2)

#Enviando notificaciones
evento.enviar_notificacion(f"{evento.nombre} se llevará a cabo el {evento.fecha} a las {evento.hora} en {evento.ubicacion}")

#Gestionando logística
evento.gestionar_logistica()

#Mostrar participantes
evento.mostrar_participantes()

