#include <iostream>
using namespace std;

void modificarPorValor(int x) {
    x += 10;
}

void modificarPorReferencia(int& x) {
    x += 10;
}

int main() {
    int numero = 20;

    cout << "Valor inicial: " << numero << endl;
    modificarPorValor(numero);
    cout << "Después de modificarPorValor: " << numero << endl;
    modificarPorReferencia(numero);
    cout << "Después de modificarPorReferencia: " << numero << endl;

    return 0;
}
