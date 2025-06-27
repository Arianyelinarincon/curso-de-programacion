mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print(mi_diccionario)
mi_diccionario["edad"]=31
print("despues de añadir edad",mi_diccionario)

mi_diccionario["profesion"]="ingeniero"
print("profesion:", mi_diccionario["profesion"])ghhhhf

print("logitud del diccionario", len(mi_diccionario))


#ejercicio
Clase={
    "Arianyelina":15,
    "Brian":10,
    "Carlos":18,
    "Damian":13,
    "Deicel":13,
    "Elias":18,
    "Fabian":17,
    "Franklin" :17,
    "Helyanni" :16,
    "Liliana":14,
    "Maria":16,
    "Over":16,
    "Paul" :14,
    "Ronald" :12,
    "Yuliexy" :10,
}
print("Notas de los estudiantes:", Clase)
Clase["Arianyelina"]= 21
Clase["Brian"]= 21
Clase["Carlos"]= 21
Clase["Damian"]= 20
Clase["Deicel"]= 17
Clase["Elias"]= 20
Clase["Fabian"]= 21
Clase["Franklin"]= 20
Clase["Helyanni"]= 21
Clase["Liliana"]= 20
Clase["Maria"]= 24
Clase["Over"]= 15
Clase["Paul"]= 19
Clase["Ronald"]= 21
Clase["Yuliexy"]= 21


print("edades de los estudiantes", Clase)

print("el nombre 'arianyelina' esta en la lista?", "Arianyelina" in Clase)

for clave in Clase:
    print(f"Nombre: {clave}, Nota: {Clase[clave]}")

#conjuntos
conjunto={1, 2, 3, 4, 5}
print("el numero 3 esta en el conjunto_?", 3 in conjunto)

conjunto.add(6)
print("Se añadio 6 al conjunto:", conjunto)

conjunto.add(3)
print (conjunto)

conjunto.remove(2)
print("se elimino el 2:", conjunto)

conjunto.discard(3)
print("se elimina el 3 de forma segura:", conjunto)

#longitud
print("longitud del conjunto:", len(conjunto))

for elemento in conjunto:
    print("elemento del conjunto:", elemento)

     #tipo de conjunto
print("el tipo de conjunto es:", type(conjunto))

otroconjunto={1, 4, 5, 6}
print("el conjunto es igual al otro?:", conjunto == otroconjunto)

#diferente !=
conjuntoa= {1, 2, 3}
conjuntob= {3, 4, 5}
print("union a y b:", conjuntoa | conjuntob)
print("union a y b:", conjuntoa & conjuntob)
print("union a y b:", conjuntoa - conjuntob)