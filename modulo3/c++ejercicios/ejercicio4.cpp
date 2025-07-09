#include <iostream>
#define LIMITE 10 
using namespace std;

int main() {
    int numero;

    cout << "Ingrese un número para ver su tabla de multiplicar: ";
    cin >> numero;

    cout << "\n📊 Tabla de multiplicar del " << numero << " hasta " << LIMITE << ":\n\n";

    for (int i = 1; i <= LIMITE; i++) {
        cout << numero << " x " << i << " = " << numero * i << endl;
    }

    return 0;
}
