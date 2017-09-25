def calcular_fuerza(masa, aceleracion):
    """ float, float --> float
    OBJ: Calcula la fuerza dado la masa y la aceleracion
    PRE: masa >= 0; aceleracion >=0"""
    return masa*aceleracion


masa = float(input("Ingrese la Masa: "))
aceleracion = float(input('Ingrese la Aceleracion: '))
print('La Fuerza dado Mass = ' + str(masa) + ' y Acelaracion: ' + str(aceleracion) + ' es: ' + str(calcular_fuerza(masa,aceleracion)))