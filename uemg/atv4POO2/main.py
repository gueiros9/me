from procgen import clear, pausa
from banco import Banco
from dolar import CotacaoDolar
from cep import enderecoCEP

# -----------------------------------
# Funções
# -----------------------------------
def Listar():
    """Lista os registros existentes na tabela
    """    
    db.select("select * from produto")

    for dados in db.dados:
        print(dados)

    pausa()

def Criar():
    """Cria a tabela necessária
    """
    db.create()
    pausa()

def Inserir():
    """Insere os dados
    """
    Nome_do_Produto = input("Digite o nome: ")
    Quantidade = input("Digite a quantidade: ")
    Valor = input("Digite o valor: ")
    dados = (Nome_do_Produto, Quantidade, Valor)
    db.insert(dados)
    pausa()

def Excluir():
    """Exclui um registro
    """
    id = input("Digite o id: ")
    db.delete(id)

    pausa("Registro excluído")

def Alterar():
    """Altera os dados
    """

    # Primeiro eu pego o id a ser alterado
    id = input("Digite o id: ")
    db.select_one(id)
    for dados in db.dados:
        print(dados)

    # Agora peço os dados para serem alterados
    Nome_do_Produto = input("Digite o nome: ")
    Quantidade = input("Digite a quantidade: ")
    Valor = input("Digite o valor: ")
    dados = (Nome_do_Produto, Quantidade, Valor, int(id) )

    db.update(dados)

    pausa()

def Entrada():
    """Realiza a entrada de produtos no estoque
    """

    #Primeiro pego o id a ser somado
    id = input("Digite o id: ")
    db.select_one(id)
    for dados in db.dados:
        print(dados)
  
    #Entrada é o que tinha antes mais o que entrou (soma)
    Nome_do_Produto = input("Digite o nome: ")
    Inicial = int(input("Digite a quantidade atual do produto: "))
    Entrada = int(input("Digite a quantidade de entrada do produto: "))
    Quantidade = int(Inicial + Entrada)
    Valor = input("Digite o valor: ")
    dados = (Nome_do_Produto, Quantidade, Valor, int(id) )

    db.update(dados)

    pausa()

def Saida():
    """Realiza a saída de produtos no estoque
    """

    #Primeiro pego o id a ser subtraído
    id = input("Digite o id: ")
    db.select_one(id)
    for dados in db.dados:
        print(dados)
  
    #Saída é o que tinha antes menos o que entrou (subtração)
    Nome_do_Produto = input("Digite o nome: ")
    Inicial = int(input("Digite a quantidade atual do produto: "))
    Entrada = int(input("Digite a quantidade de saída do produto: "))
    Quantidade = int(Inicial - Entrada)
    Valor = input("Digite o valor: ")
    dados = (Nome_do_Produto, Quantidade, Valor, int(id) )

    db.update(dados)

    pausa()

def valorDolar():
    """Lista os registros existentes na tabela com o valor em dolar
    """    
    
    dolar = CotacaoDolar()
    dolar.consulta()
    print("Valor do Dólar ",float(dolar.valor))
    print("")
        
    db.select(
      "SELECT produto.Nome_do_Produto, produto.Valor FROM produto"
      )
    
    for dados in db.dados:
        print(dados)
    
    print("")
    db.select("SELECT CAST(sum(produto.Valor) AS float) AS Total_Produtos FROM produto")

    for dados in db.dados:
        print("Valor total de produtos: ", sum(dados))
    
    soma_produtos = sum(dados)
    valor_dolar = float(dolar.valor)
    dolar_produto = valor_dolar * soma_produtos
    print("")
    print("Valor total de produtos no estoque em dólar ", dolar_produto)
 
    pausa()

def AtualizarValor():
    """Atualiza os valores
    """
    # Primeiro eu pego o id a ser atualizado
    id = input("Digite o id: ")
    db.select_one(id)
    for dados in db.dados:
        print(dados)

    # Agora peço os dados para serem atualizados
    Nome_do_Produto = dados[1]
    Quantidade = dados[2]
    Valor_atual = float(dados[3])
    Percentual = float(input("Digite o percentual de ajuste: "))
    Valor = Valor_atual + (Valor_atual * Percentual)/100
    dados = (Nome_do_Produto, Quantidade, Valor, int(id) )

    db.update(dados)

    pausa()

def buscaCEP():
    """Busca o endereço através de um CEP
    """
    numero = input("Digite somente os números do CEP: ")
    endereco = enderecoCEP(numero)
    print("")
    print (endereco.consulta())

    pausa()

 
# -----------------------------------
# Abre o banco
# -----------------------------------
db = Banco()

# -----------------------------------
# Laço principal
# -----------------------------------
while True:
    clear()
    print('''    JL Comércio LTDA
    -----------------
    1 - Listar Produtos
    2 - Inserir Produto
    3 - Excluir Produto
    4 - Alterar Produto
    5 - Entrada no Estoque
    6 - Saída do Estoque
    7 - Listar Produtos com Valor Dólar
    8 - Atualizar Valor 
    9 - Consulta CEP
    10 - Sair
    ''')
    opcao = input('Opção: ')

    if (opcao=="1"): 
        Listar()

    if (opcao=="2"): 
        Inserir()

    if (opcao=="3"): 
        Excluir()

    if (opcao=="4"): 
        Alterar()

    if (opcao=="5"):
        Entrada()       
         
    if (opcao=="6"):
        Saida()
        
    if (opcao=="7"):
        valorDolar()
        
    if (opcao=="8"):
        AtualizarValor()

    if (opcao=="9"):
        buscaCEP()            

    if (opcao=="10"): 
        exit()