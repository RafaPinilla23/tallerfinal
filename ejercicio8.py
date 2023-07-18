class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def obtener_tareas(self):
        return self.tareas


class Tarea:
    def __init__(self, nombre, descripcion, asignado_a):
        self.nombre = nombre
        self.descripcion = descripcion
        self.asignado_a = asignado_a
        self.completada = False

    def completar_tarea(self):
        self.completada = True

    def obtener_estado(self):
        return "Completada" if self.completada else "Pendiente"

    def obtener_informacion(self):
        return f"{self.nombre} - {self.descripcion} - Asignado a: {self.asignado_a}"


class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)
    
    #MetodoNuevo
    def eliminar_miembro(self, miembro):
        if miembro not in self.miembros:
            print("Miembro no encontrado")
        else:
            self.miembros.remove(miembro)

    def obtener_miembros(self):
        return self.miembros


# Crear proyecto
proyecto1 = Proyecto("Proyecto 1")

# Crear equipo
equipo1 = Equipo("Equipo 1")

#Agregar miembros al equipo
equipo1.agregar_miembro("Juan")
equipo1.agregar_miembro("María")
equipo1.agregar_miembro("Pedro")

#Crear tareas y asignarlas a miembros del equipo
tarea1 = Tarea("Tarea 1", "Realizar análisis de requerimientos", "Juan")
tarea2 = Tarea("Tarea 2", "Desarrollar funcionalidad principal", "María")
tarea3 = Tarea("Tarea 3", "Realizar pruebas de integración", "Pedro")

#Agregar tareas al proyecto
proyecto1.agregar_tarea(tarea1)
proyecto1.agregar_tarea(tarea2)
proyecto1.agregar_tarea(tarea3)

#Completar una tarea
tarea1.completar_tarea()

#Obtener información del proyecto
print(f"Información del proyecto: {proyecto1.nombre}")
print("Tareas:")
for tarea in proyecto1.obtener_tareas():
    print(tarea.obtener_informacion())
    print(f"Estado: {tarea.obtener_estado()}\n")

#Eliminar miembro
equipo1.eliminar_miembro("Pedro")

#Obtener información del equipo
print(f"Información del equipo: {equipo1.nombre}")
print("Miembros:")
for miembro in equipo1.obtener_miembros():
    print(miembro)
