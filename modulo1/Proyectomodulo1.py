#Yo se que con los emojis parece muy echo con ia, pero es que con emojis queda mas god
#asi que busque emojis que me gustaran y los puse

nombres = []
precios = []

print("🛒 Bienvenido a tu cesta de la compra 🧺")

while True:
    print("\n📋 Menú:")
    print("1️⃣ Agregar un nuevo elemento")
    print("2️⃣ Mostrar el contenido de la cesta de la compra")
    print("3️⃣ Eliminar un elemento")
    print("4️⃣ Calcular el total")
    print("5️⃣ Renunciar")

    opcion = input("👉 Elige una opción: ")

    if opcion == "1":
        nombre = input("🆕 ¿Qué artículo deseas agregar?: ")
        precio = float(input("💰 ¿Cuál es su precio?: "))
        nombres.append(nombre)
        precios.append(precio)
        print("✅ Artículo agregado.")

    elif opcion == "2":
        if len(nombres) == 0:
            print("🪹 La cesta está vacía.")
        else:
            print("📦 Contenido de la cesta:")
            for i in range(len(nombres)):
                print(f"{i+1}. {nombres[i]} - 💵 ${precios[i]:.2f}")

    elif opcion == "3":
        if len(nombres) == 0:
            print("🚫 No hay nada que eliminar.")
        else:
            for i in range(len(nombres)):
                print(f"{i+1}. {nombres[i]} - ${precios[i]:.2f}")
            numero = int(input("❓ ¿Cuál deseas eliminar?: "))
            nombres.pop(numero - 1)
            precios.pop(numero - 1)
            print("🗑️ Artículo eliminado.")

    elif opcion == "4":
        total = sum(precios)
        print(f"🧾 El total es: 💲${total:.2f}")

    elif opcion == "5":
        print("👋 Gracias por usar el programa. ¡Hasta luego!")
        break

    else:
        print("⚠️ Opción inválida. Intenta otra vez.")