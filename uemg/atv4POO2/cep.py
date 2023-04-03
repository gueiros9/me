import requests

class enderecoCEP():
    """Classe para verificar endereço através de uma API pública"""

    def __init__(self, CEP):
        self.CEP = CEP

    def consulta(self):
        url = "https://cep.awesomeapi.com.br/json/"+str(self.CEP)
        retorno = requests.get(url)
        if (retorno.status_code == 200):
          jsonparsed = retorno.json()
          return jsonparsed['address'] + "," + jsonparsed['district'] + "," + jsonparsed['city'] + "-" + jsonparsed['state']
        else:
          return "CEP inválido"