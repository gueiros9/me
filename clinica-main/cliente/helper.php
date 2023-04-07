<?php
include_once ('../config.php');

$val_M = mysqli_real_escape_string($conn, $_GET["value"]);
$result= mysqli_query($conn, "SELECT * FROM medicos JOIN categoria ON  medicos.tipo = categoria.id
WHERE categoria.id='$val_M'");
if (mysqli_num_rows($result)>0) {
  	echo '<select name = "nome" >';
 	while ($rows= mysqli_fetch_assoc($result)) {
		echo "<option>".$rows["nome"]."</option>";
	}
	echo "</select>";
} else {
	echo '<select name = "nome" >';
    $result= mysqli_query($conn, "SELECT nome FROM medicos ");
    while ($rows= mysqli_fetch_assoc($result)) {
		echo "<option>".$rows["nome"]."</option>";
	}
	echo "</select>";
}?>