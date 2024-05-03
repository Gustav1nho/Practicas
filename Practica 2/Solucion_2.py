"""- Agregar un atributo saldo a la clase persona (ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2 por consiguiente deberá
ir actualizando también el saldo o monto que tiene la otra persona en su
cuenta cada vez que use el método transferencia"""
from datetime import datetime

class Persona:
    Nombre = ""
    Edad = 0
    Nacionalidad = "Peruana"
    def __init__(self,nombre,edad):
        try:
            self.Nombre = nombre
            self.Edad = edad
        except (TypeError, KeyError):
            "Inserte parametros adecuados"
    def Descripcion(self):
        print(f"Usted es {self.Nombre} y tiene {self.Edad} años")
    def Cumpleaños(self):
        self.Edad = self.Edad + 1
        print(f"Feliz cumpleaños!! ahora tienes {self.Edad}")
    def Hora(self):
        self.año = 2022
        time_now = datetime.strptime(f"{self.año}/12/15 10:30:00", "%Y/%m/%d %H:%M:%S")
        if self.Edad == self.Edad:
            print(f"El tiempo era  {time_now}")
        else: self.Edad == self.Edad + 1
        time_now = datetime.strptime(f"{self.año+1}/12/15 10:30:00", "%Y/%m/%d %H:%M:%S")
        print(f"El tiempo ahora es : {time_now}")
class Empleado(Persona):
    def __init__(self,nombre,edad,saldo):
        super().__init__(nombre,edad)
        self.__Saldo = saldo
    def MostrarSaldo(self):
        print(f"Usted es {self.Nombre} y tiene un saldo de {self.__Saldo} soles")
    def Transferencia(self,amigo):
        self.monto = int(input("Ingrese un monto de transferencia: "))
        self.__Saldo = self.__Saldo - self.monto
        if self.__Saldo <= 0:
            print("Su saldo es insuficiente")
        else:
            amigo.__Saldo = amigo.__Saldo + self.monto
            print(f"Se ha hecho una transferencia a {amigo.Nombre} de monto {self.monto} soles")

persona1 = Empleado("Gustavo",18,5000)
persona2 = Empleado("Gabriel",19,1000)
persona1.MostrarSaldo()
persona1.Transferencia(persona2)
persona2.MostrarSaldo()