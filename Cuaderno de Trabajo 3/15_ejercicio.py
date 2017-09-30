import math
from validarEntero import validar_entero

def calcular_raices(a,b,c):
    results = []
    descriminante = calcular_descriminante(a,b,c)
    if  descriminante == 0:
        results.append = -b/(2*a)
    elif descriminante > 0:
        results.append((-b + math.sqrt(descriminante))/(2*a))
        results.append((-b - math.sqrt(descriminante))/(2*a))
    else:
        results.append('Raices imaginarias')

    return results

def calcular_descriminante(a,b,c):
    res =  b**2 -(4*a*c)
    print(res)
    return res

print('*** Programa para calcular raices de 2do grado ***')
a = input('Ingrese el valor de a: ')
b = input('Ingrese el valor de b: ')
c = input('Ingrese el valor de c: ')

if validar_entero(a) == False or validar_entero(b) == False or validar_entero(c) == False:
    print('Los valores de a,b y c deben ser enteros')
    exit(1)

a,b,c = int(a), int(b), int(c)

result = calcular_raices(a,b,c)
print('Las raices de la ecuacion son: ' + str(result))