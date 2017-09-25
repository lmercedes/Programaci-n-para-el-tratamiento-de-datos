def calcular_tabla_multiplication(numero):
    """ int --> none
    OBJ: imprimir la tabla de multiplicar de un numero hasta 10 """
    count = 1
    while count <= 10:
        print(str(numero) + ' x ' +  str(count) + ' = ' + str(numero*count))
        count += 1
    

numero = (int(input('Ingrese el numero a calcular tabla de multiplicar: ')))
calcular_tabla_multiplication(numero)
        
