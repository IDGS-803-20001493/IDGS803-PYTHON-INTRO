class operaciones():

    x = 0
    y = 0

    def suma(self):
        return self.x + self.y

    def resta(self):
        return self.x - self.y

    def multiplicacion(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y


def main(opcion):

    obj = operaciones()
    obj.x = float(input("Introduce el primer numero"))
    obj.y = float(input("Introduce el segundo numero"))

    if(opcion == 5):
        print("Cerrando programa")
    if(opcion == 1):
        print(obj.suma())
    elif(opcion == 2):
        print(obj.resta())
    elif(opcion == 3):
        print(obj.multiplicacion())
    elif(opcion == 4):
        print(obj.division())

def elejir():
    print(" 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Salir")
    opcion = int(input("Selecciona una opcion"))
    main(opcion) 

if __name__=="__main__":
    elejir()