<?php

require 'vendor/autoload.php';
use Symfony\Component\Yaml\Parser;

function get_concurs_results($edicio){
    $concurs = array();
    $concurs['guanyador'] = array();
    $concurs['finalistes'] = array();
    $concurs['seleccionats'] = array();

    $files = glob('images/'.$edicio.'/*.jpg');
    foreach ($files as $file) {

        $file_name = basename($file, '.jpg');
        $yaml_content = file_get_contents('images/'.$edicio.'/'.$file_name.'.yaml');
        $yaml = new Parser();
        $info = $yaml->parse($yaml_content);

        // Primer Premi
        if(stripos($file_name, '1er') === 0){
            $concurs['guanyador'] = array( 'file' => $file, 'info' => $info);
        }

        // Finalistes
        if(stripos($file_name, 'fin') === 0) {
            $concurs['finalistes'][] = array( 'file' => $file, 'info' => $info);
        }

        // Seleccionades.
        if(stripos($file_name, 'sel') === 0) {
            $concurs['seleccionats'][] = array( 'file' => $file, 'info' => $info);
        }

        //$concurs[$file_name] =  $info;
    }

    return json_encode($concurs);
}

function get_concurs_edicions(){
    $edicions = array();

    $edicions[] = array('xxxviii' => '2014');

    return json_encode($edicions);
}

/* Main */
if (isset($_GET["edicions"])){
    echo get_concurs_edicions();
    exit(0);
}

if(isset($_GET['edicio'])){
    echo get_concurs_results($_GET['edicio']);
    exit(0);
}

echo get_concurs_results('last');
?>
