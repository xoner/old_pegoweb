<?php
require 'vendor/autoload.php';
use Symfony\Component\Yaml\Parser;

function get_concurs_results(edicio){
    $concurs = array();
    $concurs['guanyador'] = array();
    $concurs['finalistes'] = array();
    $concurs['seleccionats'] = array();

    $files = glob('images/xxxviii/*.jpg');
    foreach ($files as $file) {

        $file_name = basename($file, '.jpg');
        $yaml_content = file_get_contents('images/xxxviii/'.$file_name.'.yaml');
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

    $edicions[] = array('any' => '2014', 'edicio' => 'xxxviii');

    return json_encode($edicions);
}

/* Main */
if (isset($_GET["edicions"])){
    echo get_concurs_edicions();
    exit(0);
}

if(isset($_GET['results']))
?>
