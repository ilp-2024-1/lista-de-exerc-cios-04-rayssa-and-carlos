# #Questão1

# linhas = int(input("Digite o número de linhas:"))
# colunas = int(input("Digite o número de colunas:"))

# matriz = [[0 for _ in range(linhas)]for _ in range(colunas)]

# for i in range(linhas):
#     for j in range(colunas):
#         matriz[i][j] = int(input("Digite um número inteiro e positivo"))
#         if  matriz[i][j] < 0:
#             matriz[i][j] *= -2


# print(matriz)

#Questão2

linhas = int(input("Digite o número de linhas:"))
colunas = int(input("Digite o número de colunas:"))

matriz = [[0 for _ in range(colunas)]for _ in range(linhas)]

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = int(input("Digite um número inteiro e positivo"))
    print("\n")   



matriz2 = [[0 for _ in range(colunas)]for _ in range(linhas)]
matriz3 = [[0 for _ in range(colunas)] for _ in range(linhas)]


for i in range(linhas):
    for j in range(colunas):
        matriz2[i][j] = int(input("Digite um número inteiro e positivo"))


for i in range(linhas):
      for j in range(colunas):
        if matriz[i][j] > matriz2[i][j]:
         matriz3[i][j] = 1
        elif matriz[i][j] < matriz2[i][j]:
           matriz3[i][j] = 2
        else: matriz3[i][j] = 0

print(matriz, end= "\n")

print(matriz2, end= "\n")

print(matriz3)

#Questão3

