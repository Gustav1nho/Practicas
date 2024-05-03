"""Reglas:
- El programa deberá tener una función para ingresar dos datos
por consola.
- Deberá tener una función en el caso haya una división entre cero
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos, mencionar el error
- Deberá tener una función donde se ingresarán N datos a una lista y al
momento de pedir un índice incorrecto para mostrarlo en consola y no
exista respectivamente ese índice, aplicar try, except
respectivamente.
- Todas las funciones creadas tendrán la facultad de volver a pedir el
número hasta que se ingresen correctamente."""


class ManejoErrores:
    def __init__(self):
        self.numm = 0

    def Suma(self,num1,num2):
        try:
            suma = int(self.num1) + int(self.num2)
            print(suma)
        except ValueError:
            print("No puedes sumar datos string aqui!!")

    def Division(self,num1,num2):
        try:
            division = int(self.num1) / int(self.num2)
            print(division)
        except (ZeroDivisionError, ValueError):
            print("Elige una variable operable! y distinta de 0 claro ")

    def Lista(self):
        lista = []
        try:
            self.cantidad = int(input("Cuantos datos quieres ingresar? "))
        except (ValueError, AttributeError):
            print("Ingresa valores numericos!")
        try:
            for i in range(0, self.cantidad):
                self.ingresar = input("Ingresa un elemento: ")
                lista.append(self.ingresar)
        except (AttributeError):
            print("Ingresa valores numericos!!")
        print(lista)
operador = ManejoErrores()
var1 = input("Ingrese un valor numerico: ")
var2 = input("Ingrese un valor numerico: ")
operador.Lista()
