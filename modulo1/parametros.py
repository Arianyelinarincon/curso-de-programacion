def sumar(a,b):
    resultado=a+b
    return resultado

valor_suma = sumar(10, 5)
print(valor_suma)

def funcionconarg(*args):
    print("argumentos posicionales:", args)
    for arg in args:
        print(f"Argumento:{arg}")