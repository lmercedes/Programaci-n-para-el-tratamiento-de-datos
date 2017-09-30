# Ejercicio #13

menu = {"L":"Arroz con Pollo",
        "M":"Paella",
        "X": "Pescado con patatas",
        "J": "Calamares en su tinta",
        "V": "Merluza empanizada",
        "S": "Cocido",
        "D": "Paella de Mariscos"}

dia = input('Introduzca el Dia: ')

if len(dia) > 1:
    print('Entrada no valida. Contiene mas de 1 caracter')
    exit(1)

if dia in menu:
    print(menu[dia])
else:
    print('Esta letra no pertenece a dia de la semana')
