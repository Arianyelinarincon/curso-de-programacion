<?php

$num1 = 12;
$num2 = 4;

$suma = $num1 + $num2;
$resta = $num1 - $num2;
$multiplicacion = $num1 * $num2;
$division = $num1 / $num2; 
$modulo = $num1%$num2;

echo "Número 1:". $num1. "\n";
echo "Número 2:". $num2. "\n";
echo "Suma:". $suma. "\n";
echo "Resta:". $resta. "\n";
echo "Multiplicación: ".$multiplicacion. "\n";
echo "División:". $division. "\n";
echo "Módulo:".  $modulo. "\n";


$metododepago="transferencia";
 switch ($metododepago) {
    case 'pago movil':
        echo "Aca estan los datos del pago movil: 9798554, 04125585474, BNC";
        break;
    case 'transferencia':
        echo "Aca estan los datos: 0102555544585458, 9854745, bnc";
        break;
    case 'zelle':
        echo "Elegiste zelle!, te damos los datos en un momento";
        break;
    case 'efectivo':
        echo "En un momento te damos tus productos!";
        break;
    default: 
        echo "metodo de pago no disponible";
        break;
 }
?>


