#expressoes regulares, procurando e-mails

#email@dominio.com.be padrao email

#99 98989 9898 padrao telefone

#123.12.12.1 padrao de ip

# import re

# string_teste ='O gato, a gata, os gatinhos, os gatoes'
# padrao = re.search(r'gat\w', string_teste)   #r - transforma em row string, tira os caracteres especiais dela com o \n 
#                                                 #o . simboliza que pode ser qualquer caracter depois dos caracteres especificado
#                                                 #\w-indentifica qualquer caracter de tipo word(palavra-Aa-zZ)
# if padrao:
#   print(padrao.group())    #imprimir o padrao de texto
# else:
#   print('padrao não encontrado')






# string_teste ='O gato, a gata, os gatinhos, os gatoes'
# padrao = re.findall(r'[]', string_teste)    #+ = repete o ultimo padrao por 1 ou mais vezes
#                                                   #* = repete o o ultiomo padro especificado 0 ou mais vezes
# if padrao:
#   print(padrao)    #imprimir o padrao de texto
# else:
#   print('padrao não encontrado')












# import requests
# requisicao = requests.get  ('https://www.pratafina.com.br/atendimento')
# string_teste =''
# padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text) #expressao feita para encontar emails

# if padrao:
#   print(padrao)    #imprimir o padrao de texto
# else:
#   print('padrao não encontrado')