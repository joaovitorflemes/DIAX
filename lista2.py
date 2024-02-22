#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
# num1 = int(input('digite o numero: '))
# num2 = int(input('digite outrovalor'))
# soma = num1 + num2 
# if soma > 10:
#     print(f'resultado: {soma}')
# 

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.

# num1 = int(input('digite o valor: '))
# num2 = int(input('digite outro valor: '))
# soma = num1 + num2
# if soma > 20:
#     print(f'resultado: {soma+8}')
# else:
#     print(f'resultado: {soma-5}')

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
# valor = int(input('digite um numero: '))
# if valor % 3 == 0:
#    print(f'É multiplo de 3')
# else:
#     print(f'nao e multiplo de 3')

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
# num1 = int(input('digite um valor: '))
# if num1 % 5 == 0:
#     print(f'e divisivel por 5:')
# else:
#     print(f'ele nao e divisivel por 5 !!')

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
# num1 = int(input('informe um valor: '))
# if num1 % 3 == 0 and num1 % 7 == 0:
#     print(f' {num1} e divisivel por 3 e por 7 !!')
# elif num1 % 3 == 0:
#     print(f'{num1} e divisivel so por 3!!') 

# elif num1 % 7 == 0:
#     print(f'{num1} e divisivel so por 7!!')
 

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
# salario_bruto = float(input('valor do salario bruto: R$ '))
# valor_prestacao = float(input('informe o valor da prestaçao: '))
# porcetagem = salario_bruto * (30/100)
# if valor_prestacao <= porcetagem:
#     print('emprestimo concedido!')
# else:
#     print('emprestimo nao autorizado!')

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
# numero = int(input('informe um numero: '))
# if numero > 20 and numero < 50:
#     print(f' {numero} esta entre 20 e 50')
# else:
#     print(f'{numero} nao esta entre 20 e 50')

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
# numero = int(input('digite um valor :'))
# if numero > 20:
#     print('maior do que 20')
# elif numero == 20:
#     print('igual a 20')
# else:
#     print('menor do que 20')  

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
#ano_nascimento = int(input('informe o ano em que vc nasceu: '))
#ano_atual = int(input('informe o ano atual: '))
#idade = ano_atual - ano_nascimento
#print(f'idade: {idade}')

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
# num1 = int(input('digite um numero inteiro: '))
# num2 = int(input('digite um numero inteiro: '))
# num3 = int(input('digite um numero inteiro: '))
# if num1<num2<num3:
#     print(f'{num1} - {num2} - {num3}')
# if num1<num3<num2:
#     print(f'{num1} - {num3} - {num2}')
# if num2<num1<num3:
#     print(f'{num2} - {num1} - {num3}')
# if num3<num2<num1:
#     print(f'{num3} - {num2} - {num1}')
# if num2<num3<num1:
#     print(f'{num2} - {num3} - {num1}')
# if num3<num1<num2:
#     print(f'{num3} - {num1} - {num2}')




#11. Faça um programa que leia 3 números e imprima o maior deles.
# num1 = float(input('digite um numero:'))
# num2 = float(input('digite um numero:'))
# num3 = float(input('digite um numero:'))
# if num1>num2 and num1>num3:
#     print(f'{num1}')
# if num2>num1 and num2>num3:
#     print(f'{num2}')
# if num3>num2 and num3>num1:
#     print(f'{num3}')



#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idade
#• Se é maior de 65 anos
# idade = int(input('digite a sua idade: '))
# if idade>18:
#     print('maior de idade')
# if idade<18:
#     print('menor de idade')
# if idade>65:
#     print('maior de 65 anos')


#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).
# nome = input('nome do aluno : ')
# nota1 = float(input('digite a primeira nota: '))
# nota2 = float(input('digite a segunda nota: '))
# media = (nota1 + nota2) / 2
# print(f'aluno : {nome} \n nota 1 prov: {nota1} \n nota 2 prova: {nota2} \n media: {media}')
# if media>=7:
#     print('aprovado')
# if media<=3:
#     print('reprovado')
# if media>3 and media<7:
#     print('recuperaçao')

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%
# salario = float(input('informe o seu salario: '))
# if salario <= 600:
#     print(f'insento : {salario}')
# if salario > 600 and salario < 1200:
#     print(f'salario teve um desconto de 20% (salario):{salario - (salario*20/100)} ')
# if salario > 1200 and salario < 2000:
#     print(f'salario teve um desconto de 25% (salario):{salario - (salario*25/100)}')
# if salario > 2000:
#     print(f'salario teve um desconto de 30% (salario):{salario - (salario*30/100)}')

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.
# produto = float(input('digite o valor do produto: '))
# valor_produto1 = produto + (produto*45/100)
# valor_produto2 = produto + (produto*30/100)
# if produto < 20:
#     print(f' valor do produto: {produto} ---- valor de venda: {valor_produto1}')
# elif produto > 20:
#     print(f' valor do produto: {produto} ---- valor de venda: {valor_produto2}')

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos
 
# idade = int(input(' informe a sua idade : '))

# if idade >= 5 and idade <= 7:
#     print('Infantil A 5 - 7 anos')
# if idade >= 8 and idade <= 10:
#     print('Infantil B 8 - 10 anos')
# if idade >= 11 and idade <= 13:
#     print('Juvenil A 11 - 13 anos')
# if idade >= 14 and idade <= 17:
#     print('Juvenil B 14 - 17 anos')
# if idade >= 18:
#     print('Sênior maiores de 18 anos')


#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

# idade = int(input('digite sua idade :'))
# if idade < 10:
#     print('Até 10 anos R$30,00')
# if idade > 10 and idade < 29:
#     print('Acima de 10 até 29 anos R$60,00')
# if idade > 29 and idade < 45:
#     print('Acima de 29 até 45 anos R$120,00')
# if idade > 45 and idade < 59:
#     print('Acima de 45 até 59 anos R$150,00')
# if idade > 59 and idade < 65:
#     print('Acima de 59 até 65 anos R$250,00')
# if idade > 65: 
#     print('Maior que 65 anos R$400,00')

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.
# mes = int(input('digite um numero de 1 a 12: '))
# if mes == 1:
#     print('mes de janeiro!!')
# if mes == 2:
#     print('mes de fevereiro!!')
# if mes == 3:
#     print('mes de março!!')
# if mes == 4:
#     print('mes de abril!!')
# if mes == 5:
#     print('mes de maio!!')
# if mes == 6:
#     print('mes de junho!!')
# if mes == 7:
#     print('mes de julho!!')
# if mes == 8:
#     print('mes de agosto!!')
# if mes == 9:
#     print('mes de setembro!!')
# if mes == 10:
#     print('mes de outubro!!')
# if mes == 11:
#     print('mes de novembro!!')
# if mes == 12:
#     print('mes de dezembro!!')
# elif mes > 12:
#     print('não existe mês com este número!!')
    
#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".
# jogador1 = float(input('digite os pontos obtidos: '))
# jogador2 = float(input('digite os pontos obtidos: '))
# jogador3 = float(input('digite os pontos obtidos: '))
# soma = jogador1 + jogador2 + jogador3
# media = (jogador1 + jogador2 + jogador3) / 3
# if jogador1 > jogador2 > jogador3:
#     print(f'{jogador1} - {jogador2} - {jogador3}')
# if jogador2 > jogador1 > jogador3:
#     print(f'{jogador2} - {jogador1} - {jogador3}')
# if jogador3 > jogador2 > jogador1:
#     print(f'{jogador3} - {jogador2}')
# if jogador2 > jogador3 > jogador1:
#     print(f'{jogador2} - {jogador3} - {jogador1}')
# if jogador3 > jogador1 > jogador2:
#     print(f'{jogador3} - {jogador1} - {jogador2}')
# if jogador1 > jogador3 > jogador2:
#     print(f'{jogador1} - {jogador3} - {jogador2}')
# if soma > 100:
#     print(f'{media}')
# elif soma < 100 :
#     print('Equipe desclassificada')

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio
# saldo_medio = float(input("Digite o saldo médio do cliente: "))
# valor_credito = saldo_medio - saldo_medio * (2/100)
# if saldo_medio <= 500:
#     print('0 a 500 nenhum crédito!!')
# elif valor_credito <= 1000:
#     print(f'valor do credito : {valor_credito * (30/100)}')
# elif valor_credito <= 3000:
#     print(f'valor do credito : {valor_credito * (40/100)}')
# else:
#     print(f'valor do credito : {valor_credito * (50/100)}')

# print(f'{saldo_medio}')


#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:
# livro = input('nome do livro: ')
# usuário = input('professor ou aluno: ')
# dias = int(input('digite o total de dias: '))
# print(f'recibo \n {livro} \n {usuário} \n {dias} ')
# if dias > 4 and dias <= 10:
#     print('somento profesores')
# if dias <= 3:
#     print('alunos')
#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.


#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano 180cal Abacaxi 75cal   Chá 20cal
#Peixe 230cal   Sorvete diet 110cal Suco de laranja 70cal
#Frango 250cal  Mousse diet 170cal  Suco de melão 100cal
#Carne 350cal   Mousse chocolate 200cal Refrigerante diet 65cal

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.
# placa = input('placa veiculo:')
# mes = placa[len(placa) -1]
# print(f'{mes}')

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos