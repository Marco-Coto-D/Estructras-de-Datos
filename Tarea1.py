class Productos:
    def __init__(self, ID, nombre, precio, paisOrigen, cantidad):
        self.ID = ID
        self.nombre = nombre
        self.precio = precio
        self.paisOrigen = paisOrigen
        self.cantidad = cantidad

    def toString(self):
        return f"ID: {self.ID}, Nombre: {self.nombre}, Precio: {self.precio}, País de Origen: {self.paisOrigen}, Cantidad: {self.cantidad}"


class Pais:
    def __init__(self, paisOrigen):
        self.paisOrigen = paisOrigen
        self.frecuencia = 1

    def toString(self):
        return f"País: {self.paisOrigen}, Frecuencia: {self.frecuencia}"

class Node:
    def __init__(self, Producto):
        self.anterior = None
        self.Producto = Producto
        self.next = None


class ListaDoble:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertar(self, producto):
        new_node = Node(producto)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.anterior = self.tail
            self.tail.next = new_node
            self.tail = new_node


    # Implementar recursividad
    # def mostrar(self):
    #   current = self.head
    #    while current is not None:
    #        print(current.Producto.toString())
    #        current = current.next

    def eliminar(self, ID):
        current = self.head
        while current is not None:
            if (current.Producto.ID == ID):
                if (current.anterior is not None):
                    current.anterior.next = current.next
                else:
                    self.head = current.next
                if (current.next is not None):
                    current.next.anterior = current.anterior
                else:
                    self.tail = current.anterior
                return
            current = current.next
        print("Producto no encontrado")

    def buscarID(self, ID):
        current = self.head
        while current is not None:
            if (current.Producto.ID == ID):
                return current.Producto
            current = current.next
        return None

    def buscarPais(self, paisOrigen):
        current = self.head
        while current is not None:
            if (current.Producto.paisOrigen == paisOrigen):
                return current.Producto
            current = current.next
        return None

    def enCero(self):
        cola_ProdVacios = []
        current = self.head
        while current is not None:
            if (current.Producto.cantidad == 0):
                cola_ProdVacios.append(current.Producto)
            current = current.next
        return cola_ProdVacios

    def listaFrecuencias(self):
        frecuencias = ListaDoble()
        current = self.head
        while current is not None:
            existente = frecuencias.buscarPais(current.Producto.paisOrigen)
            if existente is None:
                frecuencias.insertar(Pais(current.Producto.paisOrigen))
            else:
                existente.frecuencia += 1
            current = current.next
        return frecuencias