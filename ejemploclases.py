class Estudiante: 
    def __init__(self, documento, nombre, telefono):
        self.documento = documento
        self.nombre = nombre
        self.telefono = telefono
    
    def mostrar_info(self):
        print("Documento:", self.documento)
        print("Nombre:", self.nombre)
        print("Teléfono:", self.telefono)

estudiante1 = Estudiante(1111, "Juan", 24848)
estudiante1.mostrar_info()
