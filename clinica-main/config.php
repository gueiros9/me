<?php
    $servername="localhost";
    $username="root";
    $password="";
    $dbname="med";

    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        echo "Connection failed: " . $conn->connect_error;
    }else{
        echo "";
    }
?>