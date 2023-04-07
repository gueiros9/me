<?php
include('protec.php');

if(isset($_POST['submit'])){
    include_once ('config.php');
    
    $atual = ($_POST['atual']);
    $nova = password_hash($_POST['nova'], PASSWORD_DEFAULT);

    $id = $_SESSION['id'];
    $user = $_SESSION['user'];

    if($user == 'med'){

        $sql_code = "SELECT senha FROM medicos WHERE id = '$id'" ;
        $sql_query = $conn->query($sql_code) or die("Falha na execução do código SQL: " );

        $senha = $sql_query ->fetch_assoc();
        $salva['senha'] = $senha['senha'];

        if($atual == $salva['senha']){
            $result = mysqli_query($conn, "UPDATE medicos SET senha = '$nova' WHERE id = $id");
        }else{
            echo "Senha atual errada.";
        }
    }
    if($user == 'cli'){

        $sql_code = "SELECT senha FROM clientes WHERE id = '$id'" ;
        $sql_query = $conn->query($sql_code) or die("Falha na execução do código SQL: " );

        $senha = $sql_query ->fetch_assoc();
        $salva['senha'] = $senha['senha'];
        echo $nova;

        if($atual == $salva['senha']){
            $result = mysqli_query($conn, "UPDATE clientes SET senha = '$nova' WHERE id = $id");
        }else{
            echo "Senha atual errada.";
        }
    }
}
?>

<!DOCTYPE html>

<html lang="pt-BR">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <title>Dados</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
            <form action="senha.php" method="POST">
            <fieldset>
                    <legend><b>Alterar senha</b></legend>
                    
                    <?php
                    if($_SESSION['user'] == 'med' ){
                        ?><a href="medico/alterar.php"><?php
                    }?><?php
                    if($_SESSION['user'] == 'cli' ){
                        ?><a href="cliente/alterar.php"><?php
                    }?>Voltar</a>
                    
                    <br><br><br>

                    <div class="inputBox">
                        <input type="password" name="atual" class="inputUser" required>
                        <label for="atual" class="labelInput">Digite sua senha atual</label>
                    </div>

                    <br>

                    <div class="inputBox">
                        <input type="password" name="nova" class="inputUser" required>
                        <label for="nova" class="labelInput">Digite sua nova senha</label>
                    </div>

                    <br><br>

                    <div class="inputBox">
                        <a href="esqueci.php">Esqueci minha senha</a>
                    </div>

                    <br><br>

                    <input type="submit" name="submit" id="submit">
                    <br>

                </fieldset>
            </form>
        </div>
    </body>
</html>