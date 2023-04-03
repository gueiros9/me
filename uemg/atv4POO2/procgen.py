from os import system, name

def clear(): 
    """Limpa a tela
    """
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def pausa(mensagem = "Pressione qualquer tecla para continuar..."):
    """Executa uma pausa, tem como opcional uma mensagem
    """
    print("")
    print(mensagem)
    system('read n1')