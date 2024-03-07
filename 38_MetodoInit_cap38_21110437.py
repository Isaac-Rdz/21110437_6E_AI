#rodriguez mendez emmanuel isaac
#21110437
#6E1
class Jugadores():

    def __init__(self, nombre, pin):
        self.nombre=nombre
        self.pin=pin
    
    def Msj1(self):
        print("Saludos " + self.nombre + ". Iniciaran de titular el proximo partido.")
    
    def Msj2(self):
        print(self.nombre + ", No fuiste convocado")
    

jug1=Jugadores("Chicharito", "14")
jug2=Jugadores("Ricardo Marín", "19")

jug1.Msj1()
jug2.Msj1()    
jug1.Msj2()