from validarEntero import validar_entero

def validar_real(entrada):
    """string --> Boolean
    OBJ: devuelve si un valor es real o no """
    result = False
    try:
        value = float(entrada)
        result = True
    except ValueError:
        print('No se puede convertir la entrada a real')
    return result


def calcular_potencia(base,potencia):
    """ real,int --> real
    OBJ: elevar un numero real a la potencia de un valor entero 
    PRE: real == numero real;
    potencia == numero entero positivo """
    
    valor = 1
    for i in range(potencia):
        valor *= base
    
    return valor

base = input('Introduzca el valor de la base: ')
potencia =  input('Introduzca el valor de la potencia: ')

if validar_real(base) == False:
    print('La base debe ser un numero Real')
    exit(1)
elif validar_entero(potencia) == False:
    print('La potencia debe ser un numero Entero')
    exit(1)

try:
    base = float(base)
    potencia = int(potencia)
except ValueError as e:
    print('Problemas convertiendo los numeros' + e)
    exit(1)

result = 0

if potencia == 0:
    result = 1
elif potencia < 0:
    try:
        result = 1 / calcular_potencia(base, abs(potencia))
    except ValueError as e:
        print('Error calculando potencia negativa')
else:
    result = calcular_potencia(base, potencia)
    

print(str(base) + ' ^ ' + str(potencia) + ' = ' + str(result))
