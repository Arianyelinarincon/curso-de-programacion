#include <iostream>

int main() {
    int opcion;

    // El bucle do-while asegura que el menú se muestre al menos una vez
    do {
        // Mostrar el menú
        std::cout << "\nMENU" << std::endl;
        std::cout << "1. Saludar" << std::endl;
        std::cout << "2. Despedirse" << std::endl;
        std::cout << "3. Salir" << std::endl;
        std::cout << "Elige una opcion: ";
        std::cin >> opcion;

       
        switch (opcion) {
            case 1:
                std::cout << "Hola estimado :D" << std::endl;
                break; 
            case 2:
                std::cout << "Adios, ten un lindo dia/noche :C" << std::endl;
                break;
            case 3:
                std::cout << "Saliste del programa" << std::endl;
                break;
            default: 
                std::cout << "Opcion invalida, intenta de nuevo" << std::endl;
                break;
        }

    } while (opcion != 3);

    return 0;
}