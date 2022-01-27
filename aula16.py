#publicando e pesquisando no twitter
#baixar a biblioteca !pip install oauth2
import oauth2
import json
import pprint
import urllib.parse

consumer_key = 'okUpHV785VYhL0JKUYYCNzMHd'
consumer_secret ='cgfQeFwB7DPPOwTRulE9PxPKZgy3CDS1telOPnMAtohsRp9f1c'

token_key = '1475893386683064426-Hzsw3SQKaEAnmwuo9f5fEY1kMfAVam'
token_secret = 'gtnD9npvXcz3mkCi4a1VTn0TY08JFK79sXoLQqL6P3tSQ'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Pesquisa: ")
qury_codificada = urllib.parse.quote(query, safe ='')
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q='+qury_codificada+ '&lang=pt')
decodificar = requisicao[1].decode()
objeto = json.loads(decodificar)
twittes = objeto['statuses']

for twit in twittes:
  print(twit['user']['screen_name'])   #este é o caminho: objeto['statuses'][aqui é o indice-09]['user']['screen_name]
  print(twit['text'])                  #objeto['statuses'][aqui é o indice-09]['text']
  print('')


