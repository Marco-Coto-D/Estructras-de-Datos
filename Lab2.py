class Node:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
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

    def lecturaDatos(self, archivo):
        try:
            with open(archivo, 'r') as file:
                    for line in file:
                        datos = line.strip()
                        if datos != "":
                            temperatura = float(datos)
                            self.insertarFinal(temperatura)
        except FileNotFoundError:
            print("Archivo no encontrado.")

    def calcularPromedio(self):
        if self.tamanio == 0:
            return 0
        suma = 0
        current = self.head
        while current is not None:
            suma += current.dato
            current = current.next
        promedio = suma / self.tamanio
        return promedio

    def esMayor(self):
        mayor = self.head.dato
        current = self.head.next
        if current is None:
            return mayor
        while current is not None:
            if current.dato > mayor:
                mayor = current.dato
            current = current.next
        return mayor

    def esMenor(self):
        menor = self.head.dato
        current = self.head.next
        if current is None:
            return menor
        while current is not None:
            if current.dato < menor:
                menor = current.dato
            current = current.next
        return menor

    def escribir_reporte(self, nombreArchivo = "Reporte.txt"):
        promedio = self.calcularPromedio()
        mayor = self.esMayor()
        menor = self.esMenor()

        with open(nombreArchivo, "w") as archivo:
            archivo.write("===================================\n")
            archivo.write("      REPORTE DE TEMPERATURAS\n")
            archivo.write("===================================\n\n")
            archivo.write(f"Temperatura mayor: {mayor} °C\n")
            archivo.write(f"Temperatura menor: {menor} °C\n")
            archivo.write(f"Temperatura promedio: {promedio} °C\n")
            archivo.write(f"Elaborado por: Marco Coto y Fabian Moya\n")

def main():

    lista1 = ListaDoble()
    lista1.lecturaDatos("datos.txt")
    print(f"El promedio de temperaturas es: {lista1.calcularPromedio()} °C")
    print(f"La temperatura mayor es: {lista1.esMayor()} °C")
    print(f"La temperatura menor es: {lista1.esMenor()} °C")

    lista1.escribir_reporte()

if __name__ == "__main__":
    main()