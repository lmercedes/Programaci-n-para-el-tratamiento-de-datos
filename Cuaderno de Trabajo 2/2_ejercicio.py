
def calcular_area_circulo(radio):
    """ float --> float
    OBJ: Calcula el area de un circulo
    PRE: radio >= 0 """
    import math
    return (math.pi * (radio**2))


def calcular_area_cuadrado(lado):
    """ float --> float
    OBJ: Calcular el area de un cuadrado
    PRE: lado >= 0 """
    return lado*lado


def calcular_area_triangulo(base, altura):
    """ float --> float
    OBJ: Calcular el area de un triangulo
    PRE: base >= 0 y altura >= 0 """
    return (base*altura)/2

#radio = float(input('Ingrese el valor de Radio: '))
#area_circulo = print('Dado el valor de radio= ' + str(radio) + ' , el area del Circulo es: ' + str(calcular_area_circulo(radio)))

#lado = float(input('Ingrese el valor de los lados: '))
#area_cuadrado = print('Dado el valor de lados= ' + str(lado) + ' , el area del Cuadrado es: ' + str(calcular_area_cuadrado(lado)))

base = float(input('Ingrese el valor de la base: '))
altura = float(input('Ingrese el valor de la altura: '))
area_triangulo = print('Dado la base=' + str(base) + ' altura= ' + str(altura) + ', el area del triangulo es: ' + str(calcular_area_triangulo(base,altura))  + ' cm2')
