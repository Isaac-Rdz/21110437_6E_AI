#rodriguez mendez emmanuel isaac
#21110437
#6E1
class Jugadores:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
    
    def muestraDatos(self):
        print("El nombre del jugador es: " + self.nombre, "Y juega de: ", self.posicion)

jugador1 = Jugadores("Chicharito", "Delantero")

jugador1.muestraDatos()

class Jugadores_Titular(Jugadores):
    def __init__(self, nombre, posicion, equipo):
        Jugadores.__init__(self, nombre, posicion)
        self.equipo = equipo

    def muestraDatos_Titular(self):
        print("El nombre del jugador es: " + self.nombre, "Juega de: " + self.posicion, "Y juega en: " + self.equipo)

jugador2 = Jugadores_Titular("Ricardo Marín", "Delantero", "Chivas" )

jugador2.muestraDatos_Titular()
    

    