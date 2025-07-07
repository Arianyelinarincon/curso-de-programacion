<?php
$pares = 0;
$impares = 0;

echo "Números del 1 al 50:\n";

for ($i = 1; $i <= 50; $i++) {
    if ($i % 2 == 0) {
        echo "$i es par\n";
        $pares++;
    } else {
        echo "$i es impar\n";
        $impares++;
    }
}

?>