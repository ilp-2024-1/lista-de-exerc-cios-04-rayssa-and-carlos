# ---- QUESTÃO 1 ----

#Escreva um programa que leia 10 valores inteiros e armazene em uma lista. O programa deve 
#imprimir no terminal quantos valores pares foram digitados pelo usuário.
#Dica: use o operador “%” para verificar se o número é par (ZERO é neutro, ZERO NÃO
#É PAR).

#lista = []
#quantidade = 0
#for i in range(10):
#    valor = int(input(f"digite seu valor desejado{i+1}: "))
#    lista.append(valor)
#    if valor %2 == 0 and valor != 0:
#        quantidade +=1
#print(f"Seus valores mencionados são: {lista}")
#print(f"A quantidade de números pares (exceto 0) é de: {quantidade}")

#Questão2

# Escreva um programa que recebe como entrada valores inteiros para criar duas listas
# de mesmo tamanho. O tamanho das listas deverá ser definido pelo usuário. O pro-
# grama deverá somar os valores pares e ímpar de cada uma das listas. Em seguida,
# comparar as somas e informar qual dos somatórios é maior ou se há um empate.

# tamanhoLista = int(input("Digite o tamanho das listas"))

# pares = 0
# pares1 = 0
# impares = 0
# impares1 = 0


# for i in range(tamanhoLista):
#     valor = int(input("Digite um número"))
#     if valor%2 == 0:
#         pares += 0
#     else :
#         impares += 0

# for j in range(tamanhoLista):
#     valor2 = int(input("Digite um número para a segunda lista"))
#     if valor2%2 == 0:
#         pares1 += 0
#     else :
#         impares1 += 0


# print(f"Soma dos pares da lista 1: {pares}")
# print(f"Soma dos pares da lista 2: {pares1}")

# if pares > pares1:
#     print("pares1 > pares2")
# elif pares < pares1:
#     print("pares1 < pares2")
# elif pares == pares1:
#     print("As duas somas são iguais")


# print(f"Soma dos impares da lista 1: {impares}")
# print(f"Soma dos impares da lista 2: {impares1}")

# if impares > impares1:
#     print("impares1 > impares2")
# elif impares < impares1:
#     print("impares1 < impares2")
# elif impares == impares1:
#     print("As duas somas são iguais")


#Questão3


#lista = []
#quantidade = 0
#for i in range(10):
#    valor = int(input(f"digite seu valor desejado{i+1}: "))
#    lista.append(valor)
#    if valor %2 == 0 and valor != 0:
#        quantidade +=1
#print(f"Seus valores mencionados são: {lista}")
#print(f"A quantidade de números pares (exceto 0) é de: {quantidade}")

#Questão4

# tamanho = int(input("Digite o tamanho das listas "))
# lista1 = []
# lista2 = []
# for i in range(tamanho):
#     valor = input("Digite um número")
#     lista1.append(valor)


# for i in range(tamanho):
#     valor = input("Digite um número")
#     lista2.append(valor)


# lista3 = lista1+ lista2
# print(f"lista1 = {lista1}")
# print(f"lista2 = {lista2}")
# print(f"lista3 = {lista3}")



# ---- QUESTÃO 5 ----

#Escreva um programa que receba como entrada uma sequência de valores inteiros.
#Para tanto, o programa deverá inicialmente solicitar ao usuário quantos valores serão
#fornecidos para análise e só depois solicitar os valores a serem analisados. A análise
#consistirá em identificar e apresentar a partir da sequência de valores fornecidos, o
#menor valor, o maior valor e a média aritmética dos valores.

#quant = int(input("escolha a quantidade de numeros desejados: "))
#valor = []

#for i in range(quant):
#    numeros = int(input(f"digite os números desejados {i+1} : "))
#    valor.append(numeros)
#maior = max(valor)
#menor = min(valor)
#media = (maior + menor) / quant

#print(f"\nSeu maior valor é: {maior} \nSeu menor valor é: {menor} \nSua média é: {media:.2f}")

#Questão6

# size = int(input("Digite o tamanho das listas "))
# listanumber = []
# listaString = []

# for i in range(size):
#     numList = int(input("Digite um número"))
#     listanumber.append(numList)

# for i in range(size):
#     string = (input("Digite uma string"))
#     listaString.append(string)

# for i in range(size):
#     if listanumber[i]%2 != 0:
#         listanumber[i] = listaString[i]
   

# print(listanumber)

#Questão7

# size = int(input("Digite um número "))
# valores = []
# media = 0

# for i in range(size):
#   num = int(input("Digite um número"))
#   valores.append(num)


# for i in valores:
#     media += i

# valorMedia = media/size

# menorValor = min(valores)
# maiorValor = max(valores)

# print(menorValor)
# print(maiorValor)
# print(valorMedia)
# print(media)

#Questão8

# strNum = input("Digite uma sequencia de números inteiros")

# lista = []

# num = strNum.split(" ")

# lista = list(map(int, num))
# print(num)
# print(lista)

#Questão9
# Escreva um programa que receba como entrada uma string várias palavras separadas
# por espaço. O programa deverá verificar e apresentar a quantidade de ocorrência de
#
# cada palavra no texto repassado como entrada para o programa. Os sinais de pontu-
# ação não devem ser contabilizados, como por exemplo “.” Ou “,”.

contagem = 0

palavras = input("Digite um texto")

lista = palavras.split(" ")

listaTratadas = []
for palavras in lista:
    if "," in palavras or "." in palavras:
        listaTratadas += [palavras[:-1]]
listaUnica = []
for i in listaTratadas:
    if i not in listaTratadas:
        listaUnica += [i]
print(listaUnica)
        

#Questão10

# for i in range(9):
#     num = int(input("Digite um valor"))

# for i in range(3):
#     for j in range(3):
        