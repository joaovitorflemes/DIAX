import random

#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
# armazenar = []
# for x in range(15):
#     armazenar.append(input('digite um numero:  '))
# print(armazenar)


#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numeradas
# lista = []
# i = 0
# for x in range(10):
#     list(input('digite 10 letras: '))
#     print(f'{i}: {lista[i]}')
#     i+=1





#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
# lista = []
# i = 0
# for x in range(15):
#     lista.append(int(input("digite um numero:  ")))
#     if lista[i] % 2 == 0:
#         print(f'{lista[i]} é par')
#     else:
#         print(f'{lista[i]} é impar')
#     i+=1



#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.
# lista = []
# i = 0
# for x in range(2):
#     lista.append(int(input('digite um numero: '))
#     if lista[i] % 6 == 0:
#         print(f'{lista[i]} é multiplo')
#     i+=1
    
    
    






#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
# alunos = []
# for x in range(15):
#     aluno = dict()
#     aluno['nome'] = input('nome: ')
#     aluno['nota1'] = float(input('nota 1: '))
#     aluno['nota2'] = float(input('nota 2: '))
#     aluno['media'] = (aluno['nota1'] + aluno['nota2']) / 2
#     aluno['situacao'] = 'APROVADO' if aluno['media']>=6 else 'REPROVADO'
#     alunos.append(aluno)
# print('NOME\tNOTA1\tNOTA2\tMEDIA\tSITUACAO')
# for a in alunos:
#     print(f'{a["nome"]}\t{a["nota1"]}\t{a["nota2"]}\t{a["media"]}\t{a["situacao"]}') 

#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.
# pessoas = []
# for x in range(20):
#     b = dict()
#     b['salario'] = float(input('salario: '))
#     b['reajuste'] = (b['salario'] * 1.8) + (b['salario'])
#     pessoas.append(b)
# print('SALARIO\tREAJUSTE')
# for a in pessoas:
#     print(f'{a["salario"]}\t{a["reajuste"]}')
    

#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%
# precos_compra = []
# precos_venda = []
# for i in range(4):
#     while True:
#         try:
#             compra = float(input(f"Digite o preço de compra da mercadoria {i+1}: "))
#             venda = float(input(f"Digite o preço de venda da mercadoria {i+1}: "))
#             precos_compra.append(compra)
#             precos_venda.append(venda)
#             break
#         except ValueError:
#             print("Por favor, digite um valor numérico válido.")
# mercadorias_lucro = 0
# for i in range(4):
#     if precos_venda[i] > precos_compra[i]:
#         mercadorias_lucro += 1
# print(f"Quantidade de mercadorias que proporcionam lucro: {mercadorias_lucro}")


#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.

# codigo = []
# for x in range(2):
#     codigos = dict()
#     codigos['codigo'] = int(input("digite o codigo do produto: "))
#     codigos['quant'] = int(input("digite a quantidade :  "))
#     codigos['vlcompra'] = float(input("digite o valor da compra : "))
#     codigos['vlvenda'] = float(input("digite o valor da venda: "))
#     codigo.append(codigos)
# print('CODIGO\tQUANTIDADE\tVALOR_COMPRA\tVALOR_VENDA')
# for a in codigo:
#     print(f'{a["codigo"]}\t    {a["quant"]}\t          {a["vlcompra"]}\t        {a["vlvenda"]}')


        
#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.
# def ler_conjunto(nome_conjunto):
#     print(f"Digite 10 números inteiros para o {nome_conjunto}:")
#     conjunto = set()
#     while len(conjunto) < 10:
#         try:
#             numeros = input(f"Digite o número {len(conjunto)+1}: ").strip()
#             conjunto.add(int(numeros))
#         except ValueError:
#             print("Por favor, digite um número inteiro válido.")
#     return conjunto

# def main():
#     print("Conjunto 1:")
#     conjunto1 = ler_conjunto("Conjunto 1")

#     print("\nConjunto 2:")
#     conjunto2 = ler_conjunto("Conjunto 2")

#     comuns = conjunto1.intersection(conjunto2)

#     print("\nElementos comuns aos dois conjuntos:")
#     if comuns:
#         for numero in comuns:
#             print(numero)
#     else:
#         print("Não há elementos comuns.")

# if __name__ == "__main__":
#     main()


#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.













#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.

#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#um vetor e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.