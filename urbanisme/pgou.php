---
layout: page_layout
title: Pla General Ordenació Urbana
section: urbanisme
jqueryui: true
customjs: |
    //$(function(){$('#accordion').accordion({allwaysOpen: false,active: false,header: 'h3',clearStyle: true});$('.acc-content-3').accordion({allwaysOpen: false,active: false,header: 'h4',clearStyle: true});$('.acc-content-4').accordion({allwaysOpen: false,active: false,header: 'h5',clearStyle: true});});
    $('#accordion').accordion({ heightStyle: "content" });$('.acc-content-3').accordion({header: 'h4',heightStyle: "content"});$('.acc-content-4').accordion({header: 'h5',heightStyle: "content"});
description: Pla genereal d'ordenació urbana del poble de Pego
---
<?php
// Page variables and functions.
$pgouPath = "PGOU";
/**
 * Converts the name of a driectory like 00_Directory_Name to be displayed on the web page
 * as "Directory Name".
 * @param string $value the Directory Name to be converted.
 */
function trasnformDirectoryName($value){
	preg_match('/\d+_(?P<name>.*)/', $value, $matches);
	
	if(isset($matches) && $matches != null){
		return str_replace('_', ' ', $matches['name']);
	}
	
	return $value;
}

function isLeaf($dirPath){
	foreach(glob($dirPath) . '/*' as $itElement){
		if(strstr($itElement, '__leaf')){
			return true;
		}
	}
	
	return false;
}

function walkPgouDirectories($dirPath, $level){
//	if(is_file()){
//		printLeafNode($dirPath, $level + 1);
//	}
	$retVal = '';
	foreach(glob($dirPath.'/*') as $itElement){
		if(is_dir($itElement)){
			$retVal .= '<h'.$level.'><a href="#">'.trasnformDirectoryName(basename($itElement)).'</a></h'.$level.'>';
			$retVal .= '<div class="acc-content-'.$level.'">'.walkPgouDirectories($itElement, $level + 1).'</div>';
		}
		else if(is_file($itElement)){
			$retVal .= '<div class="link-to-doc"><a href="'.htmlentities($itElement).'" target="_blank">'.trasnformDirectoryName(basename($itElement)).'</a></div>';
		}
	}
	
	return $retVal;
}
// end page variables and functions.

// ****************************************
// Page content start.
// ****************************************
echo '<div id="accordion">';
echo walkPgouDirectories($pgouPath, 3);
echo '</div>';
?>