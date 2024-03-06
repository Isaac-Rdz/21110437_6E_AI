#rodriguez mendez emmanuel isaac
#21110437
#6E1

print("Buen dia que desea comprar?\n\n" + 
    "Items disponibles:\n\n"+
    "Pokeballs\n\n"+
    "1.-Pokeball: 100 monedas\n\n" +
    "2.-Superball: 150 monedas\n\n" +
    "3.-Ultraball: 200 monedas\n\n" +
    "4.-Buceobal: 150 monedas\n\n" +
    "Pociones\n\n" + 
    "5.-Hiperpocion: 500 monedas\n" +
    "6.-pocion: 250 monedas\n\n" )
    
comprar = [1]

dinero = 1500

Pokeball = 100
superball = 150
ultraball = 200
Buceoball = 150

Hiperpocion = 500
pocion = 250

if 0 in comprar or comprar == []:
    print("Elige un objeto.")

if 1 in comprar:
    
    print("Elegiste una pokeball")
    dinero = dinero - Pokeball


if 2 in comprar:
    
    print("Elegiste una superball")
    dinero = dinero - superball

if 3 in comprar:
    
    print("Elegiste una Ultraball")
    dinero = dinero - ultraball

if 4 in comprar:
    
    print("Elegiste una buceoball")
    dinero = dinero - Buceoball

if 5 in comprar:
    
    print("Elegiste una Hiperpocion")
    dinero = dinero - Hiperpocion

if 6 in comprar:
    
    print("Elegiste una Pocion")
    dinero = dinero - pocion

elif dinero < 0:
    print("Cuentas con dinero insuficiente.")

if comprar == [1] or comprar == [2] or comprar == [3] or comprar == [4] or comprar == [5] or comprar == [6]:
    print("Cuentas con " + str(dinero) + " Monedas")
    print("Se añadio el/los objetos a tu mochila.")