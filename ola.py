from numpy import digitize


print('funciona!!!')
nota1 = 7
print(nota1)
print(type(nota1))
print(f'nota1 tem valor {nota1} e é do tipo {type(nota1)}')
nota2 = 7.3
print(f'nota2 tem valor {nota2} e é do tipo {type(nota2)}')
aluno = 'maria'
print(f'aluno tem valor {aluno} e é do tipo {type(aluno)}')
media = (nota1 + nota2) / 2
print(f'{aluno}\t{nota1}\t{nota2}\t{media}') #\t tabula e \n linha
#operadores basicos
soma = nota1 + nota2
divisao = nota1 / nota2
mult = nota1 * nota2
resto_div = nota1 % nota2

#ex interaçao do usuario
nome = input('digite seu nome:')
print(f'ola {nome}. seja bem vindo(a)!')

#exercicio : leia dois valores numericos e apresente o resto da divisao
num1 = int(input('digite o num1: ')) #input retorna texto/ necessario a conversão para numérico
num2 = int(input('digite outro num2: '))
rest = num1 % num2
print(f' {num1} % {num2} :{rest}')

#leia o valor do produto e o desconto em reais e apresente o valor final

valorproduto = float(input('digite o valor do produto: '))
desconto = float(input('desconto: '))
valor_final = valorproduto - desconto
print(f'valor a pagar: R$ {valor_final}')








