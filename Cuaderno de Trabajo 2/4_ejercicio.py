def calcular_media(notas):
    """ array[int] --> float
    OBJ: Calcular la media de 3 notas
    PRE: notas > 0 """
    sumatoria = 0
    for nota in notas:
        sumatoria = nota+sumatoria
    try:
        promedio = (sumatoria)/len(notas)
    except TypeError as e:
        print('Ha ocurrido un error' + e)
    return promedio


CANTIDAD_ALUNMOS = 3
count = 1
notas = []

while count <= CANTIDAD_ALUNMOS:
   nota = int(input('Ingrese el valor de la nota # ' + str(count) + ": "))
   notas.append(nota)
   count += 1
print('La nota media de 3 alumnos es: ' + str(calcular_media(notas)))