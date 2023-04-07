<?php
include_once ('../config.php');

$val_M = mysqli_real_escape_string($conn, $_GET["value"]);

$sql_code = "SELECT * FROM consultas WHERE id='$val_M'";
$sql_query = $conn->query($sql_code) or die("Falha na execução do código SQL: " );

$r= mysqli_fetch_assoc($sql_query);
echo "<a href='medico.php'> ".$r['medico']."</a>";

if (mysqli_num_rows($sql_query)>0) {
  	echo '<select name = "agenda" >';
 	while ($rows= mysqli_fetch_assoc($sql_query)) {
		echo "<option>".$rows["agenda"]." ".$rows["hora"]."</option>";
	}
	echo "</select>";
}
