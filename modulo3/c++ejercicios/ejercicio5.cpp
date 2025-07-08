#include <iostream>
using namespace std;

int main() {
    const int numeroSecreto = 7;  
    int intento;

    cout << "juego de adivinanza!" << endl;
    cout << "Adivina el número secreto entre 1 y 10" << endl;

    while (true) {
        cout << "Ingresa tu intento: ";
        cin >> intento;

        if (intento == numeroSecreto) {
            cout << "Has adivinado el número secreto." << endl;
            break;  
        } else if (intento < numeroSecreto) {
            cout << " El número secreto es más alto" << endl;
        } else {
            cout << " El número secreto es más bajo" << endl;
        }
    }

    return 0;
}