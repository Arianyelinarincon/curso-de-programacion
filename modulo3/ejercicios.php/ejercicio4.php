<?php
echo "Verifica si puedes tener licencia\n";

$edad = 8;

if (($edad >=18 ) &&($edad <=65)) {
    echo "Si puedes tener licencia";
} elseif ($edad <18) {
    echo "No puedes tener una licencia\n";
}
else {
    echo "Eres muy mayor para tener una licencia\n";
}
echo "\n";
?>