#include <iostream>
const double PI =3.1415;

void calcularperimetro (double radio);

int main(){
    double radio;

std::cout << "Introduce el radio del circulo: ";
std::cin >> radioUsuario;

   
    calcularPerimetro(radioUsuario);

    return 0;
}

void calcularPerimetro(double radio) {
    
    double perimetro = 2 * PI * radio;
    std::cout << "El perimetro del circulo es: " << perimetro << ::endl;
}