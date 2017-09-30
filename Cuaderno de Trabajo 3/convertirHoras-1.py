# Ejercicio #3-1
from datetime import datetime

horas = {0:"12",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"11",12:"12", 13:"1",14:"2", 15:"3", 16:"4",17:"5",18:"6",19:"7",20:"8",21:"9",22:"10",23:"11"}

def convertir24_horas_a_12_horas(hora):
    """int --> int
    OBJ: convertir el formato 24 horas a 12 horas
    PRE: horas >= 0 """
    return horas[hora]
suffix = 'AM'
hora_final = ''

try:
    hora_24 = input('Ingrese la hora en formato 24 horas: (hora:minutos): ')
    hora = hora_24.split(':')
except Exception as e:
    print('Error Converting the date')
    exit(1)

if hora[0] >= "12" and hora[0] <= "24":
    suffix = 'PM'
    hora_final = str(convertir24_horas_a_12_horas(int(hora[0])))
else:
    hora_final = hora[0]

print(hora_final + ':' + str(hora[1]) +  ' ' + suffix)