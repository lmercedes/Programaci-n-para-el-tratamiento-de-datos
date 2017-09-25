def es_bisiesto(anio):
    """ int --> boolean
    OBJ: Calcular si un anio es bisiesto
    PRE: anio > 0 """
    return (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0)

anio = int(input('Ingrese el Anio: '))
print(es_bisiesto(anio))