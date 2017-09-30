# Ejercicio 3
from datetime import datetime

try:
    hora_24 = datetime.strptime(input('Ingrese la hora en formato 24 horas: (hora:minutos): '),'%H:%M')
except Exception as e:
    print('Error Converting the date')
    exit(1)

print(hora_24.strftime('%I:%M %p'))
