#algoritmo de heapq
import heapq
"""EJERCICIO: estamos trabajando en una clinica y necesitamos gestionar las prioridades de los pacientes, 
anotamos el nombre del paciente, su nivel de prioridad (1 para alta prioridad, 2 para prioridad media, 3 para baja prioridad) y orden de llegada. 
Queremos asegurarnos de que los pacientes con mayor prioridad sean atendidos primero. Para esto, podemos utilizar un heap para almacenar los pacientes, usar un menu basico y sus prioridades. 
Aquí hay un ejemplo de cómo podríamos implementar esto en Python:
"""
class Paciente:
    def __init__(self, nombre, prioridad, orden_llegada):
        self.nombre = nombre
        self.prioridad = prioridad
        self.orden_llegada = orden_llegada

    def __lt__(self, other):
        if self.prioridad == other.prioridad:
            return self.orden_llegada < other.orden_llegada
        return self.prioridad < other.prioridad
class Clinica:
    def __init__(self):
        self.pacientes = []
        self.orden_llegada = 0

    def agregar_paciente(self, nombre, prioridad):
        paciente = Paciente(nombre, prioridad, self.orden_llegada)
        heapq.heappush(self.pacientes, paciente)
        self.orden_llegada += 1
        print(f"Paciente '{nombre}' agregado con prioridad {prioridad}.")

    def mostrar_pacientes(self):
        if not self.pacientes:
            print("No hay pacientes en la clínica.")
            return
        print("Pacientes en la clínica:")
        for paciente in self.pacientes:
            print(f"Nombre: {paciente.nombre}, Prioridad: {paciente.prioridad}, Orden de llegada: {paciente.orden_llegada}")
    

    def atender_paciente(self):
        if not self.pacientes:
            print("No hay pacientes para atender.")
            return
        paciente_atendido = heapq.heappop(self.pacientes)
        print(f"Atendiendo al paciente: '{paciente_atendido.nombre}' con una prioridad de: {paciente_atendido.prioridad} ' su orden de llegada: {paciente_atendido.orden_llegada}.")
# Ejemplo de uso
clinica = Clinica()
clinica.agregar_paciente("Juan", 2)
clinica.agregar_paciente("Maria", 1)
clinica.agregar_paciente("Pedro", 3)
clinica.mostrar_pacientes()
clinica.orden_llegada = 1  # Reiniciar el orden de llegada para la demostración
clinica.atender_paciente()  # Atenderá a Maria (prioridad 1)
clinica.atender_paciente()  # Atenderá a Juan (prioridad 2
clinica.atender_paciente()  # Atenderá a Pedro (prioridad 3)
clinica.atender_paciente()  # No hay pacientes para atender