from twitter import Twitter

consumer_key = 'okUpHV785VYhL0JKUYYCNzMHd'
consumer_secret ='cgfQeFwB7DPPOwTRulE9PxPKZgy3CDS1telOPnMAtohsRp9f1c'

token_key = '1475893386683064426-Hzsw3SQKaEAnmwuo9f5fEY1kMfAVam'
token_secret = 'gtnD9npvXcz3mkCi4a1VTn0TY08JFK79sXoLQqL6P3tSQ'

twitter = twitter(consumer_key, consumer_secret, token_key, token_secret)

twitter.tweet('Vamos testar')

pesquisa = twitter.search('solyd', 'pt')

for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user']['screen_name'])