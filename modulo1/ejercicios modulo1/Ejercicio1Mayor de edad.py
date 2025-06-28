#Escribe un programa que le pida al usuario su edad y determine si es mayor de edad o no.
# Considera que la mayoría de edad se alcanza a los 18 años.

edad=int(input("Cual es tu edad?"))

if edad >=18:
    print("eres mayor de edad")
    
elif edad <0:
    print("el valor no puede ser 0 o menor que 0")
      
else:
    print("eres menor de edad")
