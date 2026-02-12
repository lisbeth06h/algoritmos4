class Nodo:
    def __init__(self, nombre, cedula, prioridad):
        self.nombre = nombre
        self.cedula = cedula
        self.siguiente = None
        self.prioridad = prioridad

class Lista:
    def __init__(self):
        self.cabeza = None

    def AgregarNodoAlFinal(self, nombre, cedula, prioridad):
        nodo = Nodo(nombre, cedula, prioridad)

        if self.cabeza is None:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

        print("Nodo agregado exitosamente.")

    def MostraNodo(self):
        actual = self.cabeza
        while actual:
            print(actual.nombre, "==>", end=" ")
            actual = actual.siguiente
        print("Fin.")

         
    
    
lista = Lista()
lista.AgregarNodoAlFinal("Juan", 111, 3)
lista.AgregarNodoAlFinal("Camila", 112, 2)
lista.AgregarNodoAlFinal("Pedro", 113,1)
lista.MostraNodo()