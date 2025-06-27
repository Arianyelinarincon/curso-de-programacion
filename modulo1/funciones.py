def saludar(nombre):
    print(f"¡Hola, {nombre}!")
# Llamada a la función saludar
saludar("Juan")  # Imprime: ¡Hola, Juan!

def sumar(a,b):

    return a+b
resultado= sumar(5,3)
print(f"la suma del 5 y 3 es: {resultado}")

def multi(a, b=2):
    return a *b 
resultadomulti=multi(4)
  
print(f"La multiplicacion es: {resultadomulti}")

def calcularrectangulo(base, altura):
    return base * altura
area= calcularrectangulo(5, 3)
print(f"el area es: {area}")

def calcular_area_circulo(radio):
    """Función que calcula el área de un círculo."""
    import math  # Importa el módulo math para usar la constante pi
    return math.pi * (radio ** 2)  # Calcula el área usando la fórmula π * r^2

radio=5
area=calcular_area_circulo(radio)
print(f"el area de un circulo con radio{radio} es {area}")