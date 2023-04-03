#1) Faça um programa que pergunte um número e retorne dizendo se é um número maior ou menor que 100
'''
num = int(input("Insira um número: "))

if num > 100:
    print ("%d é maior que 100" %num)
else:
    print ("%d é menor que 100" %num)
'''

#2) Faça um programa que pergunte um número e retorne dizendo se é um número par ou ímpar. 
'''
num = int(input("Insira um número: "))

if num % 2 :
    print ("%d é Ímpar" %num)
else:
    print ("%d é Par" %num)
'''

#3) Faça um Programa que leia três números e mostre o maior deles. 
'''
priNum = int(input("Insira o primeiro número: "))
segNum = int(input("Insira o segundo número: "))
terNum = int(input("Insira o terceiro número: "))

maior = priNum

if (segNum > maior):
    maior = segNum
if (terNum > maior):
    maior = terNum

print("%d é o maior número" %maior)
'''

#4) Faça um Programa que leia três números e mostre o maior e o menor deles. 
'''
priNum = int(input("Insira o primeiro número: "))
segNum = int(input("Insira o segundo número: "))
terNum = int(input("Insira o terceiro número: "))

maior = priNum
menor = segNum

if (segNum > maior):
    maior = segNum
if (terNum > maior):
    maior = terNum

if (priNum < menor):
    menor = priNum
if (terNum < menor):
    menor = terNum

print("%d é o maior número" %maior)
print("%d é o menor número" %menor)
'''

#5) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
# e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. 
# Caso contrário mostrar tais variáveis com o conteúdo ZERO. 
'''
peso = float(input("Insira o peso: "))
execesso = 0

if (peso > 50):
    execesso = peso - 50

multa = execesso * 4
print ("O execesso de peso foi de %.2f kg" %execesso)
print ("e a multa será de R$ R$ %.2f" %multa)
'''

#6) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, 
# quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o 
# salário líquido, conforme a tabela abaixo: a. + Salário Bruto : R$ b. - IR (11%) : R$ c. - INSS (8%) : R$ d. - Sindicato ( 5%) : R$ e. = Salário Liquido : R$
'''
salHora = float(input("Insira quanto ganha por hora: "))
horas = float(input("Insira quantas horas trabalhadas no mês: ")) 

salBruto = salHora * horas
IR = salBruto * 0.11
INSS = salBruto * 0.08
Sindicato = salBruto * 0.05
salLiq = salBruto - (IR + INSS + Sindicato)

print("O salário bruto será de R$ %.2f" %salBruto)
print("O valor do Imposto de Renda será de R$ %.2f" %IR)
print("O valor do INSS será de R$ %.2f" %INSS)
print("O valor do Sindicato será de R$ %.2f" %Sindicato)
print("O salário liquido será de R$ %.2f" %salLiq)
'''

#7) Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas. 
'''
area = float(input("Insira o tamanho da área a ser pintada: "))

litros = area / 3
qntLitros = 18
custo = 80
lata = 1

while litros > qntLitros :
    lata = lata + 1
    custo = custo + 80
    qntLitros = qntLitros + 18

print("Serão necessárias %d" %lata)
print("O custo total será R$ %.2f" %custo)
'''

#8) Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 
'''
a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))
    
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Nao é um triangulo')
elif (a == b) and (a == c) :
    print('Equilatero')
elif (a==b) or (a==c) or (b==c):
    print('Isósceles')
else:
    print('Escaleno')
'''

#9) Faça um programa que pergunte um ano e retorne se ele é um ano bissexto 
'''
ano = int(input("Insira um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print ("%d é Bissexto" %ano)
else:
    print ("%d não é Bissexto" %ano)
'''

#10) Altere o programa anterior criando uma FUNÇÃO em Python que receba um ano como parâmetro e retorne uma string dizendo se é um ano bissexto ou não. 
# Pesquise por def 
'''
ano = int(input("Digite o Ano: "))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
  def ano():
    print ("Este ano é Bissexto")
  ano()

else:
  def ano():
    print("Este ano não é Bissexto")
  ano()
'''

#11) DESAFIO:  Faça  um  programa  que  pergunte  um  ano  e  depois  faça  a  contagem  desse  ano  até  2020 colocando um * na frente dos anos bissextos. 
'''
ano = int(input("Insira um ano: "))
while ano < 2020:
    ano = ano + 1
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print ("%d *" %ano)
    else:
        print (ano)
'''