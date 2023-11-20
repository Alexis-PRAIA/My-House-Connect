<?php
// Récupération des données depuis la requête GET
$jsonData = isset($_GET['data']) ? $_GET['data'] : '';

// Décodage des données JSON
$data = json_decode(urldecode($jsonData), true);

//exec("python color_picker.py $r $g $b");

// Séparation des valeurs R, G, B
list($r, $g, $b) = explode(',', $data);

// Réponse de retour vers JavaScript (peut être sous forme de JSON)
echo json_encode(['r' => $r, 'g' => $g, 'b' => $b]);



?>