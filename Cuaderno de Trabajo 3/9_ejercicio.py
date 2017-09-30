from validarEntero import validar_entero
def leer_entero_validado():
    """ nada --> int
OBJ: Solicita un entero al usuario, lo valida y lo retorna sólo
cuando se ha asegurado de que es realmente un entero
"""
result = False
while result == False:
    valor = input('Introduzca un Valor: ')
    result = validar_entero(valor)

print(str(valor) + ' es un numero entero')