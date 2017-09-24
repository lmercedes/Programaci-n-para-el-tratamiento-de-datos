# Conversion de Farenheit a Celsius

grados_farenheit = input("Ingrese los grados en Farenheit: ")
grados_celsius = (float(grados_farenheit) - 32) * (5/9)

print('La Temperatura es: ' + str(int(grados_celsius)) + ' Celsius')