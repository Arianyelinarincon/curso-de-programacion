#include <iostream>
float calculararearectangulo(float base, float altura);
int main(){
    float base, altura;
    std::cout << "ingresa la base";
    std::cin>> base;
    std::cout << "ingresa la altura";
    std::cin>> altura;

    float area = calculararearectangulo(base, altura);
    std::cout << "el area de tu rectangulo es: " <<area << std::endl;

    return 0;
}

float calculararearectangulo(float base, float altura){

    return base*altura;
}