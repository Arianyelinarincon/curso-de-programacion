#número al usuario y determine si dicho número es par y si se encuentra en el rango de 20 a 50.
numero=int(input("ingrese un numero para determinar si es par y esta en el rango entre 20 y 50: "))
espar= numero%2==0
estaenelrango = (20 <= numero <= 50)
resultado= espar and estaenelrango

print(resultado)