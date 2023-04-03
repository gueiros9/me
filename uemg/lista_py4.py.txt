#1 Faça um programa que receba dois números e retorne a soma deles
'''
def sum(num1,num2):
	return num1 + num2
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
print ("o resultado da soma é: %d" %sum(num1,num2))
'''

#2 Monte um programa que receba uma quantidade de metros e retorne em milímetro
'''
def converter( numero, unidade):
  return( numero * pow(10,-unidade))
metros = 1
while metros:
	metros = int(input("Informe um valor em metros: "))
	if (metros):
		print("milímetros: %d" %converter(metros,-3))
'''

#3 Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos
'''
dias = int(input("Dias: "))
horas = int(input("Horas: '))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
tmpSegundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print ("%10d segundos." %tmpSegundos)
'''

#4 Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário 
'''
salario = float(input("Digite o salário: "))
aumento = float(input("Digite a porcentagem do aumento: "))
salNovo= salario + ((salario * aumento)/100)
aumento = salNovo - salario
print ("Aumento de: %.2f R$" %aumento)
print ("Novo salário: %.2f R$" %salNovo)
'''

#5 Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar
'''
preco = float(input("Digite o preço: "))
desc = float(input("Digite a porcentagem: "))
valDesc = preco * desc / 100
pagar = preco - valDesc
print("valor do desconto de R$ %.2f" % valDesc)
print("O valor a pagar é de R$ %.2f" % pagar)
'''

#6 Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem
'''
dist = float(input("Distancia em Km: "))
veloc = float(input("Velocidade média: "))
tmp = dist / veloc
print ("Tempo em horas %.2f" %tmp)
'''

#7 Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
'''
C = float(input("Temperatua em Celsius: "))
F = 9 * C / 5 + 32
print ("%f Fahrenheit" %F)
'''

#8 Faça agora o contrário, de Fahrenheit para Celsius
'''
F = float(input("Temperatura em Fahrenheit: "))
C = (F - 32) / 1.8
print('%f Celsius' %C)
'''

#9 Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado
'''
dias = int(input("Quantos dias o carro foi alugado: "))
km = float(input("Quantos quilometros o carro percorreu: "))
aluguel = (dias * 60) + (km * 0.15)
print("O valor a ser pago é: R$ %.2f" %aluguel)
'''

#10 Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias
'''
qtCigarros = int(input("Quantidade de cigarros por dia: "))
qtAnos = int(input("Há quantos anos fuma: "))
perdaMin =  (qtCigarros * 10) / 1440  
perdaMin =  (qtCigarros * 10) / 1440  
perdaDia = qtAnos * 365 * (perdaMin)
print("Foram reduzidos %d dias de vida" %perdaDia)
'''

#11 Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão
'''
digitos = str(2 ** 1000000)
qtDigitos = len(digitos)
print("O total de digitos de 2 elevado a 1 Milhão é: %d" %qtDigitos)
'''