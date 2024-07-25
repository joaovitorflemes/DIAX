ord = [5,6,69,55.666,'lavar','chute',55]
print(ord)
ord.append() #adc numero a lista
ord.extend({}) #adc varios numeros a lista
ord.insert() #adc elementos em uma posiçao escolida ou em posiçao aleatoria 
for elemento in ord: # mostra elementos
    print(elemento)

clear() #remove todos os itens da lista
copy() #faz uma copia dos valores da lista
count(valor) #retorna quantas vezes o valor informado ocorre na lista
index(valor) #retorna posiçao na lista que o valor foi encontrado
pop(index) #remove e retorna o item localizado na posiçao informada
remove(valor) #remove a primeira ocorrencia o valor informado 
reverse() # inverte a ordem da lista
sort() #ordena a lista