# Lista 03

#1) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido 
# e continue pedindo até que o usuário informe um valor válido.  
'''
num = int(input("Digite um número entre 0 e 10:  ")) 
while 0 > num or 10 < num:
    num = int(input("Número invalido, Digite novamente: "))
'''

# 2) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações  
'''
login = input("Login: ")
senha = input("Senha: ")

while login == senha:
    print("Sua senha deve ser diferente do login: ")
    senha = input("Senha: ")

print("Cadastro aprovado")
'''

# 3) Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que 
# a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva 
# o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento 
'''
popula_A = 80000
taxa_A = 0.03

popula_B = 200000
taxa_B = 0.015

ano = 0
while popula_A < popula_B:
    ano += 1
    popula_A = int((1 + taxa_A ) * popula_A)
    popula_B = int((1 + taxa_B ) * popula_B)
    print("Ano %d:" % ano)
    print("Populaçao de A: %d" %popula_A)
    print("População de B: %d\n\n" %popula_B)

print("Ultrapassa no ano:", ano)
'''

# 4) Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min. 
'''
import random

lista = []
maior = 0
menor = 100

for i in range(10):
	num = random.randint(1,100)
	lista.append(num)

	if num < menor: 
		menor = num
	if num > maior:
		maior = num

lista.sort()
print (lista)
print(" Menor: %d \n Maior: %d" %(menor, maior))
'''

# 5) Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas. 
'''
import random

lista = []
par = []
impar = []

for i in range(20):
	n = random.randint(1,100)
	lista.append(n)

	if n % 2 == 0: 
		par.append(n)
	else:
		impar.append(n)

lista.sort()
par.sort()
impar.sort()

print ("LISTA = ", lista)
print ("PAR   = ", par)
print ("IMPAR = ", impar)
'''

# 6) Crie uma função em Python usando def que receba 3 números sendo a,b e c. Retorne a soma dos 3 números. 
# Mas caso algum número seja repetido ele não entra na soma. 
'''
def soma(a,b,c):
    if a == b:
        return (b + c)
    elif b == c:
        return (a + b)
    elif a == c:
        return (a + b)
    else:
        return (a + b + c)

a = float(input("Digite um número: "))
b = float(input("Digite um número: "))
c = float(input("Digite um número: "))

print (soma(a,b,c))
'''

#7 Crie um programa que exiba um menu com 3 opções: 1 – Gravar Data, 2 – Gravar nome e 3 – Sair. 
# Se for escolhida a opção 1 deverá ser criado um arquivo com o nome de data.txt e dentro dele deverá constar a data de hoje. 
# Se for escolhida a opção 2 deverá ser perguntado o nome e gravado dentro do arquivo nome.txt o nome digitado. 
# Se for escolhido a opção 3 deverá sair.
'''
import datetime
now = datetime.datetime.now()

def gravar(num):
    if (num == 1):
        with open('data.txt', 'w') as data:
            data.write(str(now))

    elif (num == 2):
        name = input("Qual nome a ser gravado: ")
        with open('nome.txt', 'w') as nome:
            data.write(name)

num = int(input(" 1 – Gravar Data, 2 – Gravar nome e 3 – Sair "))
'''

#8 Crie um programa que grave em um arquivo de nome random.txt uma lista de 20 números aleatórios entre 100 e 999. 
'''
import random

lista = []

for i in range(20):
	num = random.randint(100,999)
	lista.append(num)


lista.sort()
with open('random.txt', 'w') as randomtxt:
            randomtxt.write(str(lista))
'''

#9) Crie um programa que leia o conteúdo do arquivo random.txt e exiba na tela o terceiro e o décimo número. 
'''
randomtxt = open('random.txt', 'r')
txt = randomtxt.read()
print(txt)
'''

#10) Crie um programa que leia o conteúdo do arquivo random.txt e exiba na tela os números pares ali existentes. 
'''
lista = []
par = []
impar = []

for i in range(20):
	n = random.randint(1,100)
	lista.append(n)

	if n % 2 == 0: 
		par.append(n)
	else:
		impar.append(n)

lista.sort()
par.sort()

with open('random.txt', 'w') as randomtxt:
            randomtxt.write(str(par))

randomtxt = open('random.txt', 'r')
txt = randomtxt.read()
print(txt)
'''