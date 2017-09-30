import math

print('1. Seno')
print('2. Coseno')
print('3. Tangente')
print('4. Cotangente')
print('5. Secante')
print('6. Cosecante')

opt = input('Escoga una opcion: ')
angulo =  float(input('Digite el angulo: '))

if opt == '1':
    print(math.sin(angulo))
elif opt == '2':
    print(math.cos(angulo))
elif opt == '3':
    print(math.tan(angulo))
elif opt == '4':
    print(math.tanh(angulo))
elif opt == '5':
    print(math.asinh(angulo))
elif opt == '6':
    print(math.acosh(angulo))
    
    
    
