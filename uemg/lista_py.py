#1) Crie uma função que receba como parâmetro um número e responda se ele é divisível por 3 e por 5 ao mesmo tempo.
'''
def divisivel(num):
  if (num % 3 == 0 and num % 5 == 0):
    print ("O número %d é divisivel por 3 e por 5" %num)
  else:
    print("O número %d não pode ser divisivel por 3 e por 5 ao mesmo tempo" %num)
'''
#2) Crie uma classe em Python chamada Soma. Ela deverá ter atributos num1, num2, total e erro. Deverá ter um método chamado Somar que irá colocar a soma de num1 e num2 dentro de total. Caso a soma seja maior que 1.000 deverá deixar o total com  valor -1 e uma mensagem de erro dentro do atributo erro. Crie um código instanciando essa classe para testar.
'''
class Soma:
  def __init__(self):
    self.num1 = 0
    self.num2 = 0
    self.total = 0
    self.erro = 0
        
  def Somar(self,n1,n2):
    self.num1 = n1
    self.num2 = n2
    self.total = self.num1 + self.num2
    if self.total > 1000:
      self.total = -1
      return 'erro.resultado: ', self.total
    else:
      return 'a soma é: ', self.total
'''
#3) Crie uma classe chama Agenda. Essa classe deverá ter como atributos nome e fone. E um método chamado Gravar. Quando esse método for chamado, caso o nome não esteja em branco deverá criar um arquivo chamado dados.txt contendo o nome e telefone separados por “;”.
'''
class Agenda: 
  def __init__(self):
    self.nome = ""
    self.fone = 0

  def Gravar(self,nm,fn):
    self.nome = nm
    self.fone = fn
    if self.nome is not None:
      with open('random.txt', 'w') as randomtxt:
            randomtxt.write(str(self.nome),';',str(self.fone))
    dados = open('dados.txt', 'r')
'''
