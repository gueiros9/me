#3 Faça uma função que receba dois números e retorne a soma deles.
'''
def soma(n1, n2):
    resultado = n1 + n2
    return resultado

num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundo numero : "))
resposta = soma(num1, num2)
print("Soma: ", resposta)
'''
#4 Faça uma função que receba 3 números e retorne o maior deles.
'''
num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundo numero : "))
num3 = int(input("Terceiro numero: "))

maior = num1

if num2 > maior:
  maior = num2

if num3 > maior:
  maior = num3

print('Maior: ', maior)
'''
#5 Faça uma função que receba uma letra e retorne "vogal" ou "consoante"
'''
def vogal(letra):
    vogais = "aeiou"
    if letra.lower() not in vogais:
        return print("consoante")
    return print("vogal")

letra = input("Digite uma letra: ")
vogal(letra)
'''
#6 Faça uma função que receba dois números e retorne P para positivo ou N para negativo.
'''
def numeros(num):
  if num >= 0:
    print('P')
  else:
    print('N')

num = int(input('Digite um número: '))
print('Este número é', end=' ')
numeros(num)
'''
#7 Faça uma função que receba três parâmetros: valor, percentual e opção. Se opção for 1 o percentual será descontado do valor. Se for 2 será um acréscimo. Retorne o valor corrigido.
'''
def fun(valor, percentual, opcao):
  percentual /= 100  
  percentual *= valor

  if opcao == 1:
    valor -= percentual
  elif opcao == 2:
    valor += percentual  
    
  print(valor)
'''
#8 Faça uma função que receba uma palavra e retorne uma palavra assim "Você escreveu a palavra XXXXX e  ela  possui  Y  letras".  Ou  seja,  a  palavra  deverá  retornar  em  maiúsculas  e  mostrar  a  quantidade de letras.
'''
from collections import Counter

palavra = input()
contar = Counter(palavra)

letras = 0
for k, v in contar.items():
  letras += 1

print("Você escreveu a palavra %s e ela possui %d letras" %(palavra.upper(), letras))
'''
#9 Crie a função Reverter que receba uma palavra e retorne essa palavra escrita na ordem inversa.
'''
palavra = input('Digite uma palavra: ')
inversa = ' '.join(palavra[::-1] for palavra in palavra.split())
print('A palavra que você digitou inversa fica: {}'.format(inversa))
'''
#10 Crie a função Semvogal que receba uma palavra e retorne essa palavra escrita sem as vogais (caso existam).
'''
def Semvogal(palavra):
  novaPalavra = ''

  for letras in palavra:
      if letras not in 'aeiou':
          novaPalavra += letras

  print (novaPalavra)

palavra = input('Digite uma palavra: ')
Semvogal(palavra)
'''
#11 Crie a função SorteioDado que retorne "Cara" ou "Coroa".
'''
import random

def SorteioDado(lado):
  if (random.randint(0,1))%2==0:
    lado = 'Cara'
  else:
    lado = 'Coroa'
  print(lado)
  return lado
  
SorteioDado('')
'''
#12 Crie uma função chamada SorteioDado que retorne um número inteiro entre 1 e 6 de forma randômica.
'''
import random

def SorteioDado(lado):
  lado = random.randint(1,6)
  print(lado)
  
SorteioDado('')
'''
#13 Crie uma  função  que  receba  uma  palavra e  retorne  essa palavra  com as  letras  misturadas  de  forma randômica.
'''
from random import shuffle

def palavra(letras):
  misturar = list(letras)
  shuffle(misturar)
  print(misturar())
'''
#14 Crie a função CriaTitulo que receba uma palavra e retorne ela dentro de um quadrado desenhado com os caracteres +,-e |.
'''
def CriaTitulo(palavra):
  linha1 = '+----+'
  linha2 = '|    |'
  linha3 = '| %s |' %palavra

  espaço = '    '
  espaço2 = '  '
  linha = '----'
  
  for letras in palavra:
    linha1 = '+--'+ linha +'--+'
    linha2 = '| ' + espaço + ' |'
    linha3 = '| ' + espaço2 + palavra + espaço2 + ' |'

  print(linha1)
  print(linha2)
  print(linha3)
  print(linha2)
  print(linha1)
'''
#15 Altere a função SorteioMoeda para receber um parâmetro de quantidade de sorteios a serem feitos e retorne uma string contendo o total de pares e ímpares no resultado.
'''
import random

def SorteioDado(lado, quantidade):
  
  if (random.randint(0,1)) %2 == 0:
    lado = 'Cara'
  else:
    lado = 'Coroa'
  print(lado)
  return lado
  
SorteioDado('')
'''
#17 Crie a função Tabuada que recebacomo parâmetro um número e imprima a tabuada desse número.
'''
tabuada = int(input("Tabuada do número: "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))
'''
#18 Crie a função Valida que receba uma letra e responda Minas Gerais se for a letra M, Tocantins se for a letra T, ou "código desconhecido" se for qualquer outra letra.
'''
def estado(letra):
  if letra == 'M':
    print('Minas Gerais')
  if letra == 'T':
    print('Tocantins')
  if letra != 'M' and letra !='T':
    print('código desconhecido')
'''
#19 Crie uma função que receba como parâmetro um número e responda se ele é divisível por 3.
'''
def div(num):
  if (num % 3 == 0):
    print ("O número %d é divisivel por 3" %num)
  else:
    print("O número %d não é divisivel por 3" %num)
'''
#20 Crie uma função que receba como parâmetro um número e responda se ele é divisível por 5.
'''
def div(num):
  if (num % 5 == 0):
    print ("O número %d é divisivel por 3 e por 5" %num)
  else:
    print("O número %d não é divisivel por 5" %num)
'''
#21 Crie uma função que receba como parâmetro um número e responda se ele é divisível por 3 e por 5 ao mesmo tempo.
'''
def div(num):
  if (num % 3 == 0 and num % 5 == 0):
    print ("O número %d é divisivel por 3 e por 5" %num)
  else:
    print("O número %d não é divisivel por 3 e por 5 ao mesmo tempo" %num)
'''
#22 Crie uma função que receba a nota de 3 provas e retorne a média ponderada desses valores. A primeira prova tem peso 3, a segunda 1 e a terceira tem peso 4.
'''
def notas(prova1,prova2,prova3):
  media = (prova1 + prova2 + prova3) / 3
  if media >= 8:
    print("possitivo")
  else:
    print("negativo")
'''
#24 Crie uma função chamada AnteeSuce que receba um número e retorne com o seu antecessor e seu sucessor.
'''
def AnteeSuce(num):
  suc = num + 1
  ant = num - 1
  
  print('O sucessor de %d é %d' %(num, suc))
  print('O antecessor de %d é %d' %(num, ant))
'''