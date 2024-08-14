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