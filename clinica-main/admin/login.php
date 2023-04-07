<?php
include('../config.php');
if(isset($_POST['cpf']) || isset($_POST['senha'])) {

    if(strlen($_POST['cpf']) == 0) {
        echo "Preencha seu e-mail";
    } else if(strlen($_POST['senha']) == 0) {
        echo "Preencha sua senha";
    } else {
        
        $cpf = $conn->real_escape_string($_POST['cpf']);
        $senha = $conn->real_escape_string($_POST['senha']);

        $sql_code = "SELECT * FROM adm WHERE login = '$cpf' AND senha = '$senha'";
        $sql_query = $conn->query($sql_code) or die("Falha na execução do código SQL: " );

        $quantidade = $sql_query->num_rows;

        if($quantidade == 1) {
                                    
            $usuario = $sql_query->fetch_assoc();

            if(!isset($_SESSION)) {
                session_start();
            }

            $_SESSION['id'] = $usuario['id'];
            $_SESSION['user'] = $usuario['user'];

            header("Location: home.php");

        } else {
            echo "Falha ao logar! E-mail ou senha incorretos";
        }
    }
}                       
?>
<!DOCTYPE html>

<html lang="pt-BR">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <title>Login</title>
        <LINK rel="stylesheet" href="mdl/material.min.css">
        <script src="mdl/material.min.js"></script>
        <link rel="manifest" href="manifest.webmanifest">
        <style>

            *{
                box-sizing: border-box;
            }
    
            body{
            font-family: Arial, Helvetica, sans-serif;
            background-image: linear-gradient(to right, rgb(20, 147, 220), rgb(17, 54, 71));
        }
        .box{
            color: white;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%,-50%);
            background-color: rgba(0, 0, 0, 0.6);
            padding: 15px;
            border-radius: 15px;
            width: 20%;
        }
        fieldset{
            border: 3px solid dodgerblue;
        }
        legend{
            border: 1px solid dodgerblue;
            padding: 10px;
            text-align: center;
            background-color: dodgerblue;
            border-radius: 8px;
        }
        .inputBox{
            position: relative;
        }
        .inputUser{
            background: none;
            border: none;
            border-bottom: 1px solid white;
            outline: none;
            color: white;
            font-size: 15px;
            width: 100%;
            letter-spacing: 2px;
        }
        .labelInput{
            position: absolute;
            top: 0px;
            left: 0px;
            pointer-events: none;
            transition: .5s;
        }
        .inputUser:focus ~ .labelInput,
        .inputUser:valid ~ .labelInput{
            top: -20px;
            font-size: 12px;
            color: dodgerblue;
        }
        
        
        #submit{
            background-image: linear-gradient(to right,rgb(0, 92, 197), rgb(90, 20, 220));
            width: 100%;
            border: none;
            padding: 15px;
            color: white;
            font-size: 15px;
            cursor: pointer;
            border-radius: 10px;
        }
        #submit:hover{
            background-image: linear-gradient(to right,rgb(0, 80, 172), rgb(80, 19, 195));
        }
    
        </style>
    
    </head>
    <body>
        <div class="box">
            <form action="login.php" method="POST">
            <fieldset>
                    <legend><b>Login</b></legend>
                    <br>
                    <div class="inputBox">
                        <input type="number" name="cpf" id="cpf" class="inputUser" required >
                        <label for="cpf" class="labelInput">Login</label>
                    </div>

                    <br><br>

                    <div class="inputBox">
                        <input type="password" name="senha" id="senha" class="inputUser" required >
                        <label for="senha" class="labelInput">Senha</label>
                    </div>

                    <br><br>

                    <input type="submit" name="submit" id="submit">
                </fieldset>
            </form>
        </div>
    </body>
</html>