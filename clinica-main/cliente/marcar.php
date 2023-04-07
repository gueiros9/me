
<?php
include('protec.php');
if(isset($_POST['submit'])){
    include_once ('../config.php');
    
    $id = $_SESSION['id'];
    $nome = $_POST['nome'];
    $agenda = $_POST['agenda'];
    $hora = $_POST['hora'];

    $result = mysqli_query($conn, "INSERT INTO consultas (paciente, medico, agenda, hora) 
    VALUES ('$id', '$nome', '$agenda', '$hora')");
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Agendar Consulta</title>
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
            #data{
                border: none;
                padding: 8px;
                border-radius: 10px;
                outline: none;
                font-size: 15px;
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
    <script> function my_fun(str) {
        if (window.XMLHttpRequest) {
            xmlhttp = new XMLHttpRequest();
        } else{
            xmlhttp= new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange= function(){
            if (this.readyState==4 && this.status==200) {
                document.getElementById('poll').innerHTML = this.responseText;
            }
        }
        xmlhttp.open("GET","helper.php?value="+str, true);
        xmlhttp.send();
    }</script>
    <body>
        <div class="box">
            <form action="marcar.php" method="POST">
                <fieldset>
                    <legend><b>Agendar consultas</b></legend>

                    <a href="home.php">Voltar</a>
                    <br><br>

                    <div class="inputBox">
                        <label for="func"><b>Médico</b></label>
                        <select id="func" onchange="my_fun(this.value);">
                            <option >Médico</option>
                            <?php include_once ('../config.php');

                            $sql_code = "SELECT id, tipo FROM categoria ORDER BY tipo ASC";
                            $sql_query = $conn->query($sql_code) or die("Falha na execução do código SQL: " );
                            
                            foreach($sql_query as $option){
                                ?>
                                <option value="<?php echo $option['id']?>"><?php echo $option['tipo']; ?>
                                </option>
                                <?php
                            }?>
                        </select>
                        <div id="poll">
                            <select name = "nome">
                                <option></option>
                                <?php include_once ('../config.php');

                                $sql_code = "SELECT id, nome FROM medicos ORDER BY tipo ASC";
                                $sql_query = $conn->query($sql_code) or die("Falha na execução do código SQL: " );
                            
                                foreach($sql_query as $option){
                                    ?>
                                    <option value="<?php echo $option['id']?>"><?php echo $option['nome']; ?>
                                    </option>
                                    <?php
                                }?>
                            </select>
                        </div>
                    </div>
                    <br>                    
                    <label for="agenda"><b>Data da consulta:</b></label>
                    <input type="date" name="agenda" >
                    <br><br>
                    <label for="hora"><b>Horario da consulta:</b></label>
                    <input type="time" name="hora" >
                    <br><br>

                    <input type="submit" name="submit" id="submit">
                </fieldset>
            </form>
        </div>
    </body>
</html>