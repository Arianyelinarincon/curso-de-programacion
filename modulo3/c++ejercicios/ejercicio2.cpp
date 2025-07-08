#include <iostream>
#include <cmath>  // Para pow y sqrt
using namespace std;

int main() {
    int num1, num2;

   
    cout << "Ingrese el primer número entero: ";
    cin >> num1;
    cout << "Ingrese el segundo número entero: ";
    cin >> num2;

    
    int suma = num1 + num2;
    int resta = num1 - num2;
    int multiplicacion = num1 * num2;
    int division = (num2 != 0) ? num1 / num2 : 0;  

   
    int potencia = static_cast<int>(pow(num1, num2));
    int raizCuadrada = (num1 >= 0) ? static_cast<int>(sqrt(num1)) : -1;

    cout << "Resultados:\n";
    cout << "Suma: " << suma << endl;
    cout << "Resta: " << resta << endl;
    cout << "Multiplicación: " << multiplicacion << endl;
    if (num2 != 0)
        cout << "División (entera): " << division << endl;
    else
        cout << "División: Error (no se puede dividir entre cero)" << endl;

    cout << "Potencia (" << num1 << "^" << num2 << "): " << potencia << endl;
    if (num1 >= 0)
        cout << "Raíz cuadrada de " << num1 << ": " << raizCuadrada << endl;
    else
        cout << "Raíz cuadrada: Error (no se puede calcular la raíz de un número negativo)" << endl;

    return 0;
}
