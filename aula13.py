# import requests
# import json

# def requisicao(titulo):
#   try:
#     req = requests.get('https://www.omdbapi.com/?t='+titulo+'&type=movie'+'&apikey=1316fb5e' )
#     dicionario = json.loads(req.text)
#     return dicionario
#   except:
#     print('Erro de conexao')
#     return None

# def printar_detelhes(filme):
#   print ('Titulo: ',filme['Title'])
#   print ('Ano: ',filme['Year'])
#   print ('Atores: ',filme['Actors'])
#   print ('Diretor: ',filme['Director'])
#   print ('Nota: ',filme['imdbRating'])
#   print ('Premios:', filme['Awards'])
#   print('Poster', filme['Poster'])
#   print('')
  
# sair = False
# while not sair:
#   op = input('Escreva o nome de um filme ou Sair para fechar: ')

#   if op == 'Sair':
#     sair = True
#   else:
#     filme = requisicao(op)
#     if filme['Response'] == 'False':
#       print('Filme não encontrado')
#     else:
#       print(filme)
#       printar_detelhes(filme)


#=========================Exercicio
# def requisicao(titulo):
#   try:
#     req = requests.get('https://www.omdbapi.com/?s='+titulo+'&type=movie'+'&apikey=1316fb5e' )
#     dicionario = json.loads(req.text)
#     return dicionario
#   except:
#     print('Erro de conexao')
#     return None

# op =input('escreva o nome do filme: ')

# filme = requisicao(op)

# print (filme[{'Title'}])

#==========================Resolucao


# from requests.models import Response
# import requests
# import json

# def lista_filmes(titulo):
#   lista = []
#   for i in range(1,101):

#     try:
#       print('Pesquisando em pagina:', i)
#       rec = requests.get('https://www.omdbapi.com/?s='+titulo+'&apikey=1316fb5e&type=movie&page='+str(i))
#       resposta = json.loads(rec.text)
#       if resposta ['Response'] == 'True':
#         for filme in resposta['Search']:
#           tit = filme['Title']
#           ano = filme['Year']
#           string = titulo +' ('+ ano + ') '
#           lista.append(string)
        
#       else:
#         print('Fim das Paginas')
#         break
      
  
#     except:
#       print('Conexao Erro')

#   return lista
# sair = False
# while not sair:
#   op = input('Pesquise por um filme ou digite Sair ')
#   if op == 'Sair':
#     sair = True
#   else:
#     lista_de_filmes = lista_filmes(op)
#     print('Filmes encontrados: ')
#     for filmes in lista_de_filmes:
#       print(filmes)