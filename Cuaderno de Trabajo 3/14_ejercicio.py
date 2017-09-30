from validarEntero import validar_entero



def es_positivo( numero):
    """ array --> int
    OBJ: devuele True si un numero es postivo
    """
    return numero > 0


def es_negativo( numero):
    """ array --> int
    OBJ: devuele True si un numero es negativo
    """
    return numero < 0


def contar_numeros(cadena):
    global cantidad_negativos
    global cantidad_positivos
    for num in cadena:
        if es_negativo(num):
            cantidad_negativos += 1
        if es_positivo(num):
            cantidad_positivos += 1


cantidad_negativos, cantidad_positivos = 0,0
end = False
cadena_numeros = []

while end == False:
    numero = input('Introduzca un numero: ')

    if int(numero) == -9999:
        end = True
        break
    if(validar_entero(numero)):
        cadena_numeros.append(int(numero))

contar_numeros(cadena_numeros)
print('Cantidad de Numeros Positivos ingresados = ' + str(cantidad_positivos))
print('Cantidad de Numeros Negativos ingresados = ' + str(cantidad_negativos))

print('Cantidad de Numeros Ingresados = '+ str(len(cadena_numeros)))