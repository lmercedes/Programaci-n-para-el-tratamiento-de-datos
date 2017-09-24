# Interprete de las constantes 20, 34.5 y True

print(type(20))
print(type(34.5))
print(type(True))

min_empleados = 10
min_facturacion = 2 # MM de Euros
min_balance = 2 #MM de Euros

cant_empleados = 20
facturacion = 18
balance = 5

es_microempresa = (cant_empleados < min_empleados and facturacion < min_facturacion) or balance < min_balance

print(es_microempresa) 
print(type(es_microempresa))