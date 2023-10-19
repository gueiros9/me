import mysql.connector

def conectar():
    try:
        # Substitua as informações de conexão conforme suas configurações
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",  # Deixe vazio se não houver senha
            database="expenses_db"
        )
        if conexao.is_connected():
            print("Conexão ao banco de dados estabelecida.")
            return conexao
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def fechar_conexao(conexao):
    if conexao.is_connected():
        conexao.close()
        print("Conexão ao banco de dados fechada.")

# Testando a conexão
if __name__ == "__main__":
    conexao_teste = conectar()
    if conexao_teste:
        fechar_conexao(conexao_teste)