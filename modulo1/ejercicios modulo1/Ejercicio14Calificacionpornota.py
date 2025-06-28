calificacion = int(input("Introduce una calificación del 1 al 100: "))

if 90 <= calificacion <= 100:
    letra = "A"
elif 80 <= calificacion < 90:
    letra = "B"
elif 70 <= calificacion < 80:
    letra = "C"
elif 60 <= calificacion < 70:
    letra = "D"
elif 0 <= calificacion < 60:
    letra = "F"
else:
    letra = "Inválida" 

print(f"Tu calificación numérica es {calificacion}, y en Letra: {letra}")