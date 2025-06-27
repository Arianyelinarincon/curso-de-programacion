#Arianyelina rincon
def juego():
    inventario = []

    print("Noche oscura, 03:33 AM... Estas conduciendo tras horas de viaje por una carretera principal de un pueblo extrano.")
    print("Ves una GASOLINERA con una pizzeria abierta... Quieres ENTRAR o SEGUIR tu camino?")
    decision1 = input("> ").strip().lower()

    if decision1 == "entrar":
        print("\nEntras a la pizzeria, el aire huele a pizza quemada. Un anciano detras del mostrador te observa.")
        print("--No queda mucho abierto a esta hora --dice--. te recomiendo que si vas al 'Hotel Lali's'... mejor compra esto.")
        print("Te muestra una linterna algo desgastada.")
        print("--Las luces del hotel fallan a menudo. Algunos dicen que cuando parpadean... no estas solo.")
        print("Quieres COMPRAR la linterna o IR directamente al hotel?")
        decision2 = input("> ").strip().lower()
        
        if decision2 == "comprar":
            inventario.append("linterna")
            print("Has obtenido una linterna. Nunca sabes cuando te servira...")

            print("\nLlegas al 'Hotel Lali's'. La recepcionista sonrie sin parpadear. Te da la habitacion 6.")
            print("Ya en tu habitacion, escuchas golpes en la puerta. ABRIR o IGNORAR?")
            decision3 = input("> ").strip().lower()

            if decision3 == "abrir":
                print("\nUsas tu linterna para ver mejor... Es un hombre que pareciera no tener cara, Retrocedes y cierras la puerta.")
                print("Encuentras una CUCHILLA bajo la cama. La tomas.")
                inventario.append("cuchilla")
            elif decision3 == "ignorar":
                print("\nIntentas dormir, pero los susurros no cesan. Algo esta justo fuera de la puerta...")
                print("A la manana siguiente, todo parece normal, pero... fue real?")
                print("FINAL: Sobreviviste, pero con cicatrices mentales.")
                return
            else:
                print("Tu indecision fue tu condena. Algo entra sin aviso.")
                print("FINAL: Has muerto.")
                return

            print("\nEscuchas una alarma sonar en los pasillos del hotel. Puedes INTENTAR ESCAPAR o ESCONDERSE.")
            decision4 = input("> ").strip().lower()

            if decision4 == "intentar escapar":
                if "cuchilla" in inventario:
                    print("Usas la cuchilla para abrir una salida trasera.")
                    print("Corres hacia la carretera y escapas... por ahora.")
                    print("FINAL: Escapaste del hotel.")
                else:
                    print("No tienes nada con que defenderte. Te atrapan.")
                    print("FINAL: Falleciste en el intento.")
            elif decision4 == "esconderse":
                print("Te metes en un armario. Pasan horas... cuando sales, el hotel esta vacio y en ruinas.")
                print("FINAL: Atrapado en una dimension extrana.")
            else:
                print("Dudas demasiado... alguien ya te encontro.")
                print("FINAL: Fin tragico.") 

        elif decision2 == "ir":
            print("Decides no comprar la linterna y sales hacia el hotel.")
            print("\nLlegas al 'Hotel Lali's'. La recepcionista sonrie sin parpadear. Te da la habitacion 6.")
            print("Al entrar, notas que el interruptor de la luz no funciona. Todo esta completamente a oscuras.")
            print("De pronto, escuchas algo arrastrandose por el piso... y no puedes ver nada.")
            print("Una respiracion ajena roza tu cuello.")
            print("FINAL: No viste lo que te atrapo. Tal vez era mejor escuchar al anciano.")
            return
        else:
            print("Opcion no valida. Te distraes un momento y decides continuar al hotel.")
            print("Llegas sin linterna... El resto de la noche se siente inquietantemente opaca.")

    elif decision1 == "seguir":
        print("\nDecides continuar. La carretera se vuelve mas densa y los arboles parecen moverse.")
        print("Se te pincha una llanta en medio de la nada. Quieres REVISAR el maletero o PEDIR AYUDA con tu celular?")
        decision2 = input("> ").strip().lower()

        if decision2 == "revisar":
            print("Encuentras una barra de metal oxidada. Puede servir como defensa.")
            inventario.append("barra")
        elif decision2 == "pedir ayuda":
            print("El telefono hace una llamada automatica. Una voz contesta: 'te veo'.")
        else:
            print("Mientras dudas, luces aparecen detras de ti. Un vehiculo sin matricula se detiene.")
            print("FINAL: Tu destino quedo sellado.")
            return

        print("\nTe adentras en el bosque buscando senal... pero lo que encuentras es un antiguo refugio con simbolos extranos.")
        print("ENTRAR o CORRER?")
        decision3 = input("> ").strip().lower()

        if decision3 == "entrar":
            if "barra" in inventario:
                print("Con la barra te abres paso y espantas a una criatura que te acecha.")
                print("Escapas por una compuerta.")
                print("FINAL: Escapaste del culto forestal.")
            else:
                print("Eres atrapado por figuras encapuchadas.")
                print("FINAL: Sacrificio consumado.")
        elif decision3 == "correr":
            print("Corres sin mirar atras. Tropiezas, pero logras volver al auto y huir.")
            print("FINAL: Escapaste, pero con visiones que no desapareceran jamas.")
        else:
            print("El bosque te traga lentamente.")
            print("FINAL: Olvidado en la penumbra.")
    
    else:
        print("No entendiste las senales. El destino eligio por ti.")
        print("FINAL: Nunca llegaste a tu destino.")

juego()