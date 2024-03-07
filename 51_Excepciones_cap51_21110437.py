#rodriguez mendez emmanuel isaac
#21110437
#6E1

reinicio = True

while reinicio:
    try:
        num1 = int(input("Introduce un numero para multiplicar: "))
        num2 = int(input("Introduce otro numero para multiplicar: "))
    except ValueError:
        print("No has introducido ningun valor.")
    else:
        print("El resultado es: ", num1 * num2)
    finally:
        pregunta = input("¿Quieres hacer otra operacion? introduce S/N: \n")
    if pregunta == "N":
        reinicio = False
    else:
        print("De acuerdo, hagamos otra multiplicacion") 