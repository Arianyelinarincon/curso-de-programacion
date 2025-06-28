d= 12
e= 22
suma=d+e
resta= d-e
multi=d*e
division=d/e
division_entera=d//e
modulo=d%e
exponente=d**e
print(suma)
print(resta)
print(multi)
print(division)
print(division_entera)
print(modulo)
print(exponente)


#ejercicio1 
nombre="Andrea " 
apellido="rincon"
edad="21"
cuidad="maracaibo" 
print(f"Hola soy", nombre+apellido, "tengo", edad, "y soy de ", cuidad)

#ejercicio2
nota1= 12
nota2= 20
nota3= 1
notadefinitiva= (nota1+nota2+nota3)/3
print("la calificacion de tus notas 12, 20 y 15 es:", notadefinitiva)

#input
formulario1=input("cual es tu nombre")
print(f"tunombrees:{formulario1}")

formulario=int(input("edad: "))
print(f"tu edad es: {formulario}")

#== si son iguales true, != si no son es true, > uno mayor a otro, < uno menor a otro, <= si es menor o igual, >= si es mayor o igual

#ejercicio1 operaciones
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))

sum=numero1+numero2
res=numero1-numero2
mul=numero1*numero2
divi=numero1/numero2

print(f"el resultado de la suma es: {sum}")
print(f"el resultado de la resta es: {res}")
print(f"el resultado de la mul es: {mul}")
print(f"el resultado de la divi es: {divi}")


#ejercicio2par o impar
nume1=int(input("Ingrese el primer numero: "))
nume2=int(input("Ingrese el segundo numero: "))
res=nume1%nume2
print(f"es: {res}")

#ejerciciooperadoreslogicos
numer=int(input("Ingrese un numero del 10 al 20 "))
resultado= numer >= 10 
print(resultado)

notaA=int(input("Ingresa tu nota: "))
if notaA >= 90: 
    print(f"Sacaste una A")
elif notaA <= 90:
 print(f"Sacaste una A")


elif notaA <= 100: 
    print(f"Sacaste una A")
     
elif notaA >= 80: 
    print(f"Sacaste una B")

elif notaA <= 89: 
    print(f"Sacaste una B")

elif notaA >= 80: 
    print(f"Sacaste una B")

elif notaA <= 89: 
    print(f"Sacaste una B")