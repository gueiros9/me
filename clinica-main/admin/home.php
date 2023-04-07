<?php
include('protec.php');
?>
<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home</title>
        <style>
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
            #data_nascimento{
                border: none;
                padding: 8px;
                border-radius: 10px;
                outline: none;
                font-size: 15px;
            }
            #submit{
                background-image: linear-gradient(to right,rgb(0, 255, 255), rgb(153, 153, 255));
                width: 100%;
                border: none;
                padding: 15px;
                color: white;
                font-size: 15px;
                cursor: pointer;
                border-radius: 10px;
            }
            #submit:hover{
                background-image: linear-gradient(to right,rgb(0, 255, 255), rgb(153, 153, 255));
            }
        </style>
    </head>
    <body>
        <div class="box">
            <form action="home.php" method="POST">
                <fieldset>
                    <legend><b>Administração</b></legend>
                    <a href="logout.php">Sair</a>  

                    <br><br>
                   
                    <button type="button" id="submit"><a href="admin.php">Cadastrar novo Usuário</a> </button>

                    <br><br><br>

                    <button type="button" id="submit"><a href="clientes.php">Visualizar Clientes cadastrados</a> </button>

                    <br><br><br>

                    <button type="button" id="submit"><a href="medicos.php">Visualizar Médicos cadastrados</a> </button>

                    <br><br>

                </fieldset>
            </form>
        </div>
    </body>
</html>