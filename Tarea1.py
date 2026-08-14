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
        self.tamanio = 0

    def insertarFinal(self, producto):
        new_node = Node(producto)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tamanio += 1
            return
        else:
            new_node.anterior = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tamanio += 1
            return

    def insertarMedio(self, posicion, producto):
        if posicion < 0 or posicion > self.tamanio:
            print("Posición inválida.")
            return
        if posicion == 0:
            self.insertarFinal(producto)
            return
        if posicion == self.tamanio:
            self.insertarFinal(producto)
            return

        nuevo = Node(producto)
        current = self.head
        contador = 0
        while current is not None and contador < posicion - 1:
            current = current.next
            contador += 1

        nuevo.anterior = current.anterior
        nuevo.next = current

        current.anterior.next = nuevo
        current.anterior = nuevo

        self.tamanio += 1

        
                    


    def mostrar(self, current=None):
        if current is None:
            current = self.head
        if current is None:
            return
        print(current.Producto.toString())
        if current.next is not None:
            self.mostrar(current.next)

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
                frecuencias.insertarFinal(Pais(current.Producto.paisOrigen))
            else:
                existente.frecuencia += 1
            current = current.next
        return frecuencias

    def generarReporte(self, nombreArchivo="reporte_recuperacion.txt"):
        PrecioTotal = 0
        with open(nombreArchivo, "w") as archivo:
            current = self.head
            while current is not None:
                producto = current.Producto
                archivo.write(f"ID: {producto.ID}, Nombre: {producto.nombre}, " f"Cantidad: {producto.cantidad}, Precio: {producto.precio}\n")
                PrecioTotal += producto.cantidad * producto.precio
                current = current.next
            archivo.write(f"Total a recuperar: {PrecioTotal}\n")
        return PrecioTotal



class Menu:
    def __init__(self):
        self.lista = ListaDoble()

    def mostrarMenu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Insertar producto")
            print("2. Eliminar producto por ID")
            print("3. Buscar producto por ID")
            print("4. Mostrar productos")
            print("5. Generar reporte de recuperación")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                ID = input("Ingrese el ID del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                paisOrigen = input("Ingrese el país de origen del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                producto = Productos(ID, nombre, precio, paisOrigen, cantidad)
                self.lista.insertarFinal(producto)
            elif opcion == "2":
                ID = input("Ingrese el ID del producto a eliminar: ")
                self.lista.eliminar(ID)
            elif opcion == "3":
                ID = input("Ingrese el ID del producto a buscar: ")
                producto = self.lista.buscarID(ID)
                if producto:
                    print(producto.toString())
                else:
                    print("Producto no encontrado.")
            elif opcion == "4":
                print("Productos en la lista:")
                self.lista.mostrar()
            elif opcion == "5":
                self.lista.generarReporte()
                print("Reporte generado.")
            elif opcion == "0":
                print("Saliendo del programa.")
                break


menu = Menu()
menu.mostrarMenu()