import requests

class CotacaoDolar():
    """Classe para verificar a cotação do dolar através de uma API pública"""

    def __init__(self):
        self.valor = -1

    def consulta(self):
        url = "https://economia.awesomeapi.com.br/json/all/USD-BRL"
        retorno = requests.get(url)
        if (retorno.status_code == 200):
          jsonparsed = retorno.json()
          self.valor = jsonparsed['USD']['high']
        else:
          self.valor = -1