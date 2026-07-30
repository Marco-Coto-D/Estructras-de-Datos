class Node: 
    def __init__(self, valor):  
        self.data = valor
        self.next = None 

class SingleLinkedList:
    def __init__(self):
        self.head = None 

    def insert(self, valor): 
        new_node = Node(valor) 
        if (self.head is None): 
            self.head = new_node
            return
        current = self.head 
        while (current.next):
            current = current.next 
        current.next = new_node  

    def display(self): 
        current = self.head
        while (current): 
            print(current.data, end=" -> ")
            current = current.next 
        print("None")

    def insertar_al_inicio(self, valor):
        new_node = Node(valor)
        new_node.next = self.head  
        self.head = new_node      
    
    
    def insertar_en_medio(self, valor, posicion):
        if posicion == 0:
            self.insertar_al_inicio(valor)
            return
    
        new_node = Node(valor)
        current = self.head
        contador = 0
    
        while current is not None and contador < posicion - 1:
            current = current.next
            contador += 1
    
        if current is None:
            print("Posición fuera de rango")
            return
    
        new_node.next = current.next 
        current.next = new_node

    def eliminarEnPosicion(self, posicion):
        if self.head is None:
            print("La lista está vacía")
            return
        if posicion == 0:
            self.head = self.head.next
            return
        actual = self.head
        contador = 0
        while actual.next is not None and contador < posicion - 1:
            actual = actual.next
            contador += 1
        if actual.next is None:
            print("Posición fuera de rango")
            return
        actual.next = actual.next.next 

    def eliminarAlInicio(self):
        if self.head is None:
            print("La lista está vacía")
            return
        self.head = self.head.next

    def eliminaFinal(self):
        if self.head is None:
            print("La lista está vacía")
            return
        if self.head.next is None:
            self.head = None
            return
        actual = self.head
        while actual.next.next is not None:
            actual = actual.next
        actual.next = None

    def buscar(self, valor):
        contador = 0
        current = self.head
        while current is not None:
            if current.data == valor:
                print(f"Valor {valor} encontrado en la lista en la posición {contador}.")
                return
            current = current.next
            contador += 1
        print(f"Valor {valor} no encontrado en la lista.")

    def esVacia(self):
        return self.head is None


class Menu:
    def __init__(self):
        self.lista = SingleLinkedList()

    def mostrarMenu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Insertar al inicio")
            print("2. Insertar en medio")
            print("3. Insertar al final")
            print("4. Eliminar en posición")
            print("5. Eliminar al inicio")
            print("6. Eliminar al final")
            print("7. Revisar si la lista está vacía")
            print("8. Buscar un valor")
            print("9. Mostrar lista")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                valor = input("Ingrese el valor a insertar al inicio: ")
                self.lista.insertar_al_inicio(valor)
            elif opcion == "2":
                valor = input("Ingrese el valor a insertar en medio: ")
                posicion = int(input("Ingrese la posición donde insertar: "))
                self.lista.insertar_en_medio(valor, posicion)
            elif opcion == "3":
                valor = input("Ingrese el valor a insertar al final: ")
                self.lista.insert(valor)
            elif opcion == "4":
                posicion = int(input("Ingrese la posición a eliminar: "))
                self.lista.eliminarEnPosicion(posicion)
            elif opcion == "5":
                self.lista.eliminarAlInicio()
            elif opcion == "6":
                self.lista.eliminaFinal()
            elif opcion == "7":
                if self.lista.esVacia():
                    print("La lista está vacía.")
                else:
                    print("La lista no está vacía.")
            elif opcion == "8":
                valor = input("Ingrese el valor a buscar: ")
                self.lista.buscar(valor)
            elif opcion == "9":
                self.lista.display()
            elif opcion == "0":
                print("Saliendo del programa.")
                break


menu = Menu()
menu.mostrarMenu()   