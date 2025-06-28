#el primero es mayor que el segundo y si el segundo es mayor que el tercero.

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

resultado= (numero1>numero2) and (numero2>numero3)
print(resultado)