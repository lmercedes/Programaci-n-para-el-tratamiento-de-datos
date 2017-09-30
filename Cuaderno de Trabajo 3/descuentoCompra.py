# Descuento de compra. Ejercicio #1

DESCUENTO_5 = 0.05
DESCUENTO_2 = 0.02
EFECTIVO = 'ef'
TARJETA_CREDITO = 'tc'
total = 0.0

def es_positivo(valor):
    """ float --> boolean
    OBJ: chequea si el valor ingresado es positivo
    PRE: valor >= 0 """
    if valor >= 0:
        return True
    else:
        return False


def calcular_descuento(cantidad, tipo_pago):
    """" Float, String --> Float
    OBJ Calcula la cantidad de descuento de una compra
    dependiendo la cantidad comprada y el tipo de pago """
    descuento = 0
    if cantidad > 100:
        if tipo_pago == EFECTIVO:
            descuento = cantidad*DESCUENTO_5
        elif tipo_pago == TARJETA_CREDITO:
            descuento = cantidad*DESCUENTO_2
    return descuento

try:
    cantidad = float(input('Ingrese la cantidad comprada: '))
except:
    print('Hubo un problema con la cantidad ingresada. ')
    exit(1)

if es_positivo(cantidad) != True:
    print('Debe ingresar un numero Positivo')
    exit(1)

if cantidad <= 100:
    print('EL todal de su compra es: ' +  str(cantidad) + ' euros')
    exit()

tipo_pago = input('Ingrese el tipo de Pago (ef = Efectivo; tc = Tarjeta de Credito): ')

if tipo_pago != EFECTIVO and tipo_pago != TARJETA_CREDITO:
    print('El tipo de pago ingresado no es correcto.')
    exit()

print('EL todal de su compra es: ' +  str(cantidad - calcular_descuento(cantidad, tipo_pago)) + ' euros')
