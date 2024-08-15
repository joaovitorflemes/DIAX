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
# for i in range(100):
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

#  produtos = dict()
#     ultimo_codigo = 0
#     with open('produtos.dat','r') as arquivo:
#         for linha in arquivo:
#             campos = linha.split(';')
#             p = dict()
#             p['cod'] = int(campos[0])
#             p['nome'] = campos[1]
#             p['qtde'] = campos[2]
#             p['valor_compra'] = float(campos[3])
#             p['valor_venda'] = float(campos[4])
#             produtos[p['cod']] = p
#             ultimo_codigo = p['cod']
#     with open('produtos.dat','a') as arquivo:
#         while True:
#             p = dict()
#             p['cod'] = int(input(f'Cód({ultimo_codigo+1}): '))
#             if p['cod'] < 0:
#                 break
#             ultimo_codigo = p['cod']
#             p['nome'] = input('Nome: ').upper()
#             p['qtde'] = int(input('Qtde: '))
#             p['valor_compra'] = float(input('Valor de Compra: R$ '))
#             p['valor_venda'] = float(input('Valor de Venda: R$ '))
#             produtos[p['cod']] = p
#             arquivo.write(f'{p["cod"]};{p["nome"]};{p["qtde"]};{p["valor_compra"]};{p["valor_venda"]}\n')
#     print('LISTA DE PRODUTOS:\n')
#     for p in produtos.values():
#         print(f'{p["cod"]}\t{p["nome"]}\t{p["qtde"]}\tR$ {p["valor_compra"]}\tR$ {p["valor_venda"]}')
#     codigo = int(input('Digite o cód a ser pesquisado: '))
#     print(f'{produtos[codigo]}')


        
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

# import math

# def main():
 
#     lista_original = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]
    

#     lista_fatoriais = [math.factorial(num) for num in lista_original]

    
#     maior = max(lista_fatoriais)
#     menor = min(lista_fatoriais)

#     total_pares = sum(1 for num in lista_fatoriais if num % 2 == 0)
#     percentual_pares = (total_pares / len(lista_fatoriais)) * 100

    
#     media_fatoriais = sum(lista_fatoriais) / len(lista_fatoriais)

#     print("\nLista original:", lista_original)
#     print("Lista de fatoriais:", lista_fatoriais)
#     print("Maior valor dos fatoriais:", maior)
#     print("Menor valor dos fatoriais:", menor)
#     print(f"Percentual de números pares na lista de fatoriais: {percentual_pares:.2f}%")
#     print(f"Média dos elementos da lista de fatoriais: {media_fatoriais:.2f}")

# if __name__ == "__main__":
#     main()








#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.
# def processar_lista(lista):
#     if not lista:
#         print("A lista está vazia.")
#         return
    
#     maior = max(lista)
#     menor = min(lista)
    
#     pares = [x for x in lista if x % 2 == 0]
#     percentual_pares = (len(pares) / len(lista)) * 100
 
#     media = sum(lista) / len(lista)
    
    
#     print(f"Maior valor: {maior}")
#     print(f"Menor valor: {menor}")
#     print(f"Percentual de números pares: {percentual_pares:.2f}%")
#     print(f"Média dos elementos: {media:.2f}")


# lista = [1, 2, 3, 4, 5, 6]
# processar_lista(lista)













#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

# NUM_MESESAS = 30
# LUGARES_POR_MESA = 5
# TOTAL_LUGARES = NUM_MESESAS * LUGARES_POR_MESA
# mesas = {i: LUGARES_POR_MESA for i in range(1, NUM_MESESAS + 1)}
# lugares_ocupados = 0

# def exibir_estado_mesas():
#     """Exibe o estado atual das mesas."""
#     print("\nEstado atual das mesas:")
#     for mesa, lugares_disponiveis in mesas.items():
#         print(f"Mesa {mesa}: {lugares_disponiveis} lugares disponíveis")

# def reservar_lugares(codigo_mesa, quantidade_lugares):
#     """Tenta reservar lugares na mesa especificada."""
#     global lugares_ocupados

#     if codigo_mesa not in mesas:
#         print("Código da mesa inválido.")
#         return

#     if quantidade_lugares <= 0 or quantidade_lugares > LUGARES_POR_MESA:
#         print("Quantidade de lugares inválida. Deve ser entre 1 e 5.")
#         return

#     if mesas[codigo_mesa] >= quantidade_lugares:
#         mesas[codigo_mesa] -= quantidade_lugares
#         lugares_ocupados += quantidade_lugares
#         print(f"Reserva de {quantidade_lugares} lugar(es) na mesa {codigo_mesa} realizada com sucesso.")
#     else:
#         print(f"Não há lugares suficientes na mesa {codigo_mesa}. Apenas {mesas[codigo_mesa]} lugar(es) disponíveis.")

# def main():
#     global lugares_ocupados

#     while lugares_ocupados < TOTAL_LUGARES:
#         exibir_estado_mesas()
#         try:
#             codigo_mesa = int(input("\nDigite o código da mesa (1 a 30) ou 0 para sair: "))
#             if codigo_mesa == 0:
#                 print("Encerrando o programa.")
#                 break

#             quantidade_lugares = int(input("Digite a quantidade de lugares desejados: "))
#             reservar_lugares(codigo_mesa, quantidade_lugares)

#         except ValueError:
#             print("Entrada inválida. Por favor, insira números inteiros.")

#     if lugares_ocupados >= TOTAL_LUGARES:
#         print("Todos os lugares estão ocupados.")

# if __name__ == "__main__":
#     main()


#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.
numeros_voos = 10
lugares_disponiveis = 




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