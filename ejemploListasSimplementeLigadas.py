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
        nodo = Nodo(nombre, cedula)
        if self.cabeza == None:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                actual = actual.siguiente
            
            actual.siguiente = nodo
        print("Nodo agregado exitosamente.")
    
    def MostraNodo(self):
        actual = self.cabeza
        while actual:
            print(actual.nombre, end="==>")
            print("_____")
            actual = actual.siguiente
        print("Fin.")   

    def AgregarConPrioridad(self, nombre, cedula, prioridad):
        nodo = Nodo(nombre, cedula, prioridad)     
        if self.cabeza == None:
            self.cabeza = nodo
        elif self.cabeza.prioridad > prioridad:
            nodo.siguiente = self.cabeza
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente
            nodo.siguiente = actual.siguiente
            actual.siguiente = nodo
         
    
    
lista = Lista()
lista.AgregarNodoAlFinal("Juan", 111)
lista.AgregarNodoAlFinal("Camila", 112)
lista.AgregarNodoAlFinal("Pedro", 113)
lista.MostraNodo()