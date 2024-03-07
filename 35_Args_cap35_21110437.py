#rodriguez mendez emmanuel isaac
#21110437
#6E1


def ChivEqp ( DT, Sustituos, *args):
    print("DT: " + DT)
    print("Sustitutos: " + Sustituos)
    for x in args:
        print("Jugadores: " + x)

ListJug = ["Chicharito", "JJ Macias", "Erick Gutierrez", "Pocho Guzman"]

ChivEqp("Fernando Gago", "Ricardo Marín", *ListJug)