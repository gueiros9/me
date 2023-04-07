<?php
include('protec.php');

if(isset($_POST['submit'])){
    include_once ('../config.php');
    $id = $_SESSION['id'];

    $telefone = $_POST['telefone'];

    $result = mysqli_query($conn, "UPDATE clientes SET telefone = '$telefone' WHERE id = '$id'");
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
            <form action="alterar.php" method="POST">
            <fieldset>
                    <legend><b>Atualizar dados</b></legend>
                    
                    <a href="home.php">Voltar</a>
                    <br><br><br>

                    <div class="inputBox">
                        <?php
                        include_once ('../config.php');
                        $id = $_SESSION['id'];

                        $telefone = mysqli_query($conn,"SELECT telefone FROM clientes where id = '$id'");
                        while($row=mysqli_fetch_array($telefone)){?> 
                            <input type="telefone" name="telefone" class="inputUser"value="<?php echo $row['telefone'];?>"required><?php
                        }?>
                        <label for="telefone" class="labelInput">Telefone</label>
                    </div>

                    <br><br>

                    <div class="inputBox">
                        <a href="../senha.php">Trocar Senha</a>
                    </div>
                    
                    <br><br>

                    <input type="submit" name="submit" id="submit">

                </fieldset>
            </form>
        </div>
    </body>
</html>