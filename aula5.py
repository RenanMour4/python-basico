#estruturas de laços
# nomes = ['Renan', 'Marcio', 'Maria', 'Luana']
# lista_de_numeros = range(0, 10)
# palavra = 'Macacos me Mordam'
# lista_de_frutas=['Pera', 'Mamão', 'melao', 'abacate', 'uva', 'maca', 'banana']

# i = 0
# cont = 0
# numero = 0

# while True:
#     print(numero)
    
#     if numero == 20:
#         break
#     numero+=1
# print('Saiu do while')

# for fruta in lista_de_frutas:
#     cont += 1

# print(cont)

# while i < 10:
#     print('I ainda é menor do que 10:', i)
#     i = i +1
# print('I chegou a ', i)


# for letra in palavra:
#     print(letra)

# for i in range(len(nomes)):
#     print(nomes[i])


# for item in range(0, 20, 2):
#     print(item)

# for item in lista_de_numeros:
#     print(item)

# for nome in nomes:
#     print(nome)


'''
EXERCICIO: faça um programa que leia a quantidade de pessoas  que serão convidadas para a festa
Apos isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados
Apos isso irá imprimir na tela todos os nomes da lista
'''

qntd = int(input('Quantas pessoas serão convidadas: '))
qntd_pessoas = range(qntd)
convidados = []
lista_de_convidados = []

for pessoas in qntd_pessoas:
    convidados = input('Qual o nome do convidado? ')
    lista_de_convidados.append(convidados)


print('Lista de Convidados:')
for i in lista_de_convidados:
    print(i)



#Resolução

# print('Programinha de controle de festinhas 1.0')
# print('########################################')

# numero_de_convidados = input('Coloque o numero de convidados: ')
# lista_de_convidados = []

# i = 1
# while i <= int(numero_de_convidados):
#     nome_do_convidado = input('Coloque o nome do convidado #'+ str(i) +': ')
#     lista_de_convidados.append(nome_do_convidado)
#     i += 1

# print('Serão', numero_de_convidados, 'convidados')

# print('\nLISTA DE CONVIDADOS')
# for convidado in lista_de_convidados:
#     print(convidado)






