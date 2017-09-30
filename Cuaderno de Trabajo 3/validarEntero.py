def validar_entero(entrada):
    """string --> Boolean
    OBJ: Valida si una entrada es un numero entero o no """
    result = False
    try:
        value = int(entrada)
        result = True
    except ValueError:
        print('No se puede convertir la entrada a entero')
    return result

#no se puede convertir un string float a int? :(