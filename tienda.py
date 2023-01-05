from accounUser import Cliente
class Tienda(Cliente):
    nombre = str
    ubicacion = str
    
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion 
        