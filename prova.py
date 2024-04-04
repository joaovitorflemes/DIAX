#1. Faça um programa que leia o valor unitário de um produto,
#   a quantidade desejada e imprima o valor total a pagar. (2,5pt)
# valor = float(input('digite valor do produto: '))
# quantidade = int(input('quantidade do produto: '))
# valortotal = valor * quantidade
# print(f'valor total a pagar R${valortotal}!')

#2. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#   da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#   a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#   "Reprovado" ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#   reprovação e as demais em prova final). (2,5pt)
# nome = input('nome do aluno: ')
# nota1 = float(input('nota da prova 1 : '))
# nota2 = float(input('nota da prova 2: '))
# media = (nota1 + nota2) / 2
# if media >= 7:
#     print(f'nome do aluno: {nome} \n nota1: {nota1} \n nota2: {nota2} \n media: {media} \n "aprovado"')
# if media < 7 and media > 3 :
#     print(f'nome do aluno: {nome} \n nota1: {nota1} \n nota2: {nota2} \n media: {media} \n "prova final"')
# if media <= 3:
#     print(f'nome do aluno: {nome} \n nota1: {nota1} \n nota2: {nota2} \n media: {media} \n "reprovado"')



#3. Faça um programa que apresente um menu com 4 opções:
#   [1] - Cadastrar
#   [2] - Excluir
#   [3] - Pesquisar
#   [0] - Sair
#   O usuário deve escolher uma opção e o programa deve imprimir uma mensagem 
#   ao entrar em cada opção do menu. O programa só deve encerrar quando a opção
#   escolhida for zero (0). (2,5pt)
# opçoes = int(input('escolha uma opçao: ----- [1] - Cadastrar ----- [2] - Excluir ----- [3] - Pesquisar ----- [0] sair '))
# while True:
#     if opçoes == 0:
#         break
#     if opçoes == 1:
#         print('cadastrar usuario')
#     if opçoes == 2:
#         print('excluir usuario')
#     if opçoes == 3:
#         print('pesquisar usuario')
    
        

#4. Faça um programa que calcule o retorno de um investimento. (2,5pt)
#   O programa deve solicitar do usuário o:
#   - valor que será investido;
#   - prazo do investimento (meses);
#   - juros mensal (juros composto).
investimento = float(input('digite o valor do investimento: '))
prazo = int(input('prazo do investimento: '))
juros = float(input('juros mensal : '))





