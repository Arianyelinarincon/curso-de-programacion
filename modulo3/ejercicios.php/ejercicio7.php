<?php

$temperatura = readline("Introduce la temperatura en °C: ");

$temperatura = floatval($temperatura);

if ($temperatura < 10) {
    echo "Hace frío \n";
} elseif ($temperatura >= 10 && $temperatura <= 25) {
    echo "Está templado \n";
} else {
    echo "Hace calor \n";
}
?>
