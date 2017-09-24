texto_numerico = "45" 
print(int (texto_numerico))
# Conversion correcta. Permite convertir un texto a numero
#print(int ("Hola"))
# Error. No es posible convertir caracteres alfa a numero

print(int (3.99999))
# Conversion correcta. Es posible convertir un decimal a numero entero. Esta conversion elimina los decimales y solo toma en consideracion el entero

print(float (34))
# Conversion correcta. Es posible convertir de entero a decimal. En este ejemplo se agrega el decimal como default: 34.0