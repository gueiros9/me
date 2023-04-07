<?php
if(!isset($_SESSION)){
    session_start();

    if($_SESSION['user'] == 'med' ){
        session_reset();
    }else{
        die("Você não pode acessar esta página.");
    }

}
if(!isset($_SESSION['id'])){
    die("Você não pode acessar esta página porque não está logado.");
}
?>