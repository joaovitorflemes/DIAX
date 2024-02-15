'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
print('joao vitor')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
#print(30*27)

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
#valor = 5
#valor2 = 8
#valor3 = 12
#media = (valor + valor2 + valor3) / 3
#print(media)

#4. Faça um programa que leia e imprima um número inteiro.

#numero = int(input('digite um numero inteiro :'))
#print(numero)

#5. Faça um programa que leia dois números reais e os imprima.
#valor = float(input('digite um valor :R$ ' ))
#valor2 = float(input('digite um valor : R$ ' ))
#print(valor,valor2)


#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.

#valor = int(input('digite um valor: '))
#sucessor = valor + 1
#antecessor = valor - 1
#print(antecessor,valor,sucessor)





  
#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
#nome = input('digite o seu nome:  ')
#endereço = input('informe o seu endereço: ')
#numero = input('digite o seu numero de telefone: ')
#print(f'{nome} \n endereço: {endereço} \n numero de telefone :{numero}')


#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
#numero = int(input('digite um valor: '))
#numero2 = int(input('digite outro valor: '))
#print(numero - numero2)

#9. Faça um programa que leia um número real e imprima ¼ deste número.
#numeroreal = float(input('digite um numero real : '))
#resultado = numeroreal / 4 
#print(resultado)

#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
#nota = float(input('digite o valor: '))
#nota2 = float(input('digite o valor:'))
#nota3 = float(input('digite o valor:'))
#media = (nota + nota2 + nota3) / 3

#print(f'media do dos numeros e : {media} ')

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.

#valor1 = float(input('digite um valor: '))
#valor2 = float(input('digite um valor: '))
#print(f'adiçao: {valor1 + valor2} \n subtraçao: {valor1 - valor2} \n multiplicaçao: {valor1 * valor2} \n divisao: {valor1 / valor2}')

#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.

#valor = float(input('digite um valor real :'))
#quadrado = valor ** 2 
#print(f'o quadrado desse numero e : {quadrado}')


#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
#conta = float(input('digite o valor do saldo em conta: '))
#conversão = conta + (conta * (2 / 100))
#print(f'valor da conta e : {conversão}')


#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base + altura) e a área (base * altura).
#base = float(input('insira a base: '))
#altura = float(input('insira a altura: '))
#print(f'o perimeto : {base + altura} \n a area: {base * altura}')

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
# prodt = float(input('digite o valor do produto: '))
# desct = float(input('adicione a % de desconto : '))
# novovalor = prodt - (prodt * (desct / 100))
# desconto = prodt * (desct / 100)
# print(f'valor do desconto : {desconto} \n valor com o desconto : {novovalor}')
#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.
#salario = float(input('digite o valor do seu salario atual : '))
#desct = float(input('adicione a % de desconto : '))
#novovalor = salario + (salario * (desct / 100))
#print(f'valor do salario  : {novovalor}')

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5
#c = float(input('digite o valor do grau: '))
#F = (9 * c + 160) / 5
#print(f'o valor do grau convertido e : {F}')


#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
#tempo = float(input('digite tempo de hr gasto : '))
#velocidade = float(input('digite a velocidae: '))
#D = tempo / 60 * velocidade       
#L = D / 12

#print(f'distancia percorrida : {D} \n litros consumidos : {L}')

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
# valorprest = float(input('digite o valor da parcela em atraso: '))
# taxa = float(input('digite o valor da taxa: '))
# periodo = float(input('digite o periodo de atraso: '))

# juros = (valorprest * taxa * periodo)
# print(f'valor da prestaçao: {valorprest} \n periodo de atraso: {periodo} \n valor da taxa: {taxa} \n valor da prestaçao com acrescimo: {juros}')


#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.
# dolar = float(input('digite o valor em dólar: US$ '))
# real = dolar * 4.98
# print(f'valor convertido para real é : R$ {real:.2f}')