def calcular_puntos_dentro_circunferencia(x,y, radio):
    """ int, int --> int
    OBJ: calcular si un punto esta dentro de una circunferencia """
    import math
    return math.sqrt((x**2 + y**2)) <= radio

RADIO = 1000
x = int(input('Ingrese el valor de x: '))
y = int(input('Ingrese el valor de y: '))
print('(' + str(x) + ',' + str(y) + ') esta dentro de la circunferencia(' + str(RADIO) + '): ' + str(calcular_puntos_dentro_circunferencia(x,y,RADIO)))