#Metodos e funçoes

#função:
# print('OI!')
# len() 

# def soma(numero1, numero2):                          #definindo função            
#     resp = numero1 + numero2
#     return resp

# retorno = soma(45, 87)
# print(retorno)

# def imprime_oi():
#     print('oi')

# imprime_oi()

# def tem_sete_itens(argumento):
#     if len(argumento) == 7:
#         return True
#     else:
#         return False

# if tem_sete_itens("1234567"):
#     print('Tem sete itens')

#metodo não tem o retorno



'''
Escreva uma função que recebe um objeto de coleção
e retorna o valor do maior numero dentro dessa coleção,
faça outra funçao que retorna o valor do menor numero
'''
colecao_num = [89,3,4,-5,6,7]



def maior_numero(colecao):
    numero_maior = 0 
    for num in colecao:
        if num > numero_maior:
            numero_maior = num
    print(numero_maior)


def menor_numero(colecao):
    numero_menor = 0 
    for num in colecao:
        if num < numero_menor:
            numero_menor = num
    print(numero_menor)


maior_numero(colecao_num)
menor_numero(colecao_num)

#Resolução:

# def maior(colecao):
#     maior_item = colecao[0]
#     for item in colecao:
#         if item > maior_item:
#             maior_item = item
#     return maior_item

# def menor(colecao):
#     menor_item = colecao[0]
#     for item in colecao:
#         if item < menor_item:
#             menor_item = item
#     return menor_item

# print(menor([1,-2,1.2,87.2,1289,-7,0]))



        
        
            



