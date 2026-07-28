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


lista1=SingleLinkedList()
lista1.insert(10) 
lista1.insert(20)
lista1.insert(30)
lista1.insert(40)
lista1.insert(50)
lista1.insert(60)
lista1.display() 


    
print("Insertar al inicio: 5")
lista1.insertar_al_inicio(5)
lista1.display()
print("Insertar en medio: 25 en la posición 3")
lista1.insertar_en_medio(25, 3)
lista1.display()
print("Eliminar en posición: 9")
lista1.eliminarEnPosicion(9)
lista1.display()
print("Eliminar al inicio")
lista1.eliminarAlInicio()
lista1.display()
print("Eliminar al final")
lista1.eliminaFinal()
lista1.display()