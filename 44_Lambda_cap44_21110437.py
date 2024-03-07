#rodriguez mendez emmanuel isaac
#21110437
#6E1

import math

def area(radio):
    resultado = round(math.pi * radio*  radio, 2)
    print(resultado)

area(2)

area = lambda radio: round(math.pi * radio * radio, 2)

print(area(2))