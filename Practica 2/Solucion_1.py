"""- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad, saldo y de nacionalidad peruana (use el manejo de errores para el
tipo de dato) y un método para solicitar su nombre y edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo instanciar la clase 2 veces, mostrar por
pantalla dicha edad actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)"""

from datetime import datetime

class Persona:
    Nombre = ""
    Edad = 0
    Saldo = 0
    Nacionalidad = "Peruana"
    def __init__(self,nombre,edad,saldo):
        try:
            self.Nombre = nombre
            self.Edad = edad
            self.Saldo = saldo
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

Persona1 = Persona("daniel",20,5000)
Persona1.Descripcion()
Persona1.Cumpleaños()
Persona1.Hora()
Persona1.Cumpleaños()
Persona1.Hora()
