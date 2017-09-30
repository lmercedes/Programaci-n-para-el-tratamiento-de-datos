from validarEntero import validar_entero

meses = {1: "Enero", 2: "Febrero",3:"Marzo",
        4:"Abril",5:"Mayo", 6:"Junio",
        7:"Julio",8:"Agosto",9:"Septiembre",
        10:"Octubre",11: "Noviembre", 12: "Diciembre"}

def convertir_meses_letra(mes):
    """ string --> string
    OBJ: Dado un numero del 1-12 retornar el nombre del mes correspondiente
    PRE: >=1 mes <=12
    """
    return meses[mes]

mes = input('Ingrese el valor del mes en numero: ')
if validar_entero(mes) == True:
    mes = int(mes)
    if mes >= 1 and mes <=12:
        print(convertir_meses_letra(mes))
    else:
        print('El valor debe estar entre 1 y 12')
else:
    print('No se puede conertir este numero a mes')