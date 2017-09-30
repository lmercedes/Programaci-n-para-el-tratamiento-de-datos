from validarEntero import validar_entero
def calcular_serie_armonica(limite):
    sum = 0
    i=1
    while sum < limite:
        sum += 1/i
        i += 1
    return i -1

limite = int(input('Ingrese el limite a calcular. Debe ser un entero positivo: '))
if validar_entero(limite) == True and limite > 0:
    print(str(calcular_serie_armonica(limite)))