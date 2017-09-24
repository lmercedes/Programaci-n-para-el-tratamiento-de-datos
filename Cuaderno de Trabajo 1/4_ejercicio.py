deducion_personal = 600
deducion_por_hijos = 60

ingreso_total = 3000
cantidad_hijos = 2

ingreso_imponible = ingreso_total - deducion_personal - (deducion_por_hijos * cantidad_hijos)
impuestos_a_pagar = ingreso_imponible / 3 
print("El total de impuestos a pagar es: " +  str(impuestos_a_pagar))