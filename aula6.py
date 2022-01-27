#Estrutura de dados

# lista = ['renan', 1, 'moura', 'Re']    #mutavel
# tupla = ('Mario', 2)             #não mutavel
# dicionario = {'idade':16, 'nome': 'renan'}  
# conjunto = {'Re', 'na'}  #não existe itens repetidos, sem indice

#iniciar list, tuple, set(conjunto), dict vazios

# lista_vazio = []
# tupla_vazio= ()
# conjunto = set()
# dicionario = {}



#===========================================
# conjunto.add('euzin')
# conjunto.add('Salve')
# conjunto.remove('Re')

# if 'Re' in conjunto:
#     print('Foi encontrado')

                                   #Da o mesmo resultado, porem a lista em programas não serve muito bem para buscas, o conjunto é mais indicado para isso

# if 'Re' in lista:
#     print('Foi encontrado')

# print(conjunto[0])


#=======================================

# print(dicionario['nome'])
# print(len(dicionario))

# if 'renan' in dicionario.values():
#     print('Renan está no dicionario')

# for valores in dicionario.keys():
#     print(valores)

# dicionario['nome'] = 'joa'
# dicionario['endereco'] = 'Rua do sabão'
# print(dicionario)
      



#=======================================================
# print(type(tupla))
# for i in tupla:
#     print(i)

# tupla[0] = 'eu'
# tupla = ('Eu', 'VC')
# print(tupla)

# if 'Mario' in tupla:
#     print('Mario esta na tupla')


# loucura = [(1,2), (3,4), (5,6), ({'Jao', 'Maria'}, {'Renan'})]
# print(loucura)



dicionario = {}

dicionario['idade'] = input('Escreva sua idade')

print(dicionario['idade'])

