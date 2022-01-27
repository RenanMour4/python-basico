#Consultando a cotacao do dolar 
import json
import re
import requests
import time
import datetime



while True:
  print('### COTAÇÃO ###', datetime.datetime.now())
  requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
  cotacao = json.loads(requisicao.text)

  print('DóLAR: ',cotacao['USDBRL']['bid'])
  print('euro: ',cotacao['EURBRL']['bid'])
  print('btc: ',cotacao['BTCBRL']['bid'])
  time.sleep(2)

#Consultando Clima

cidade = input("Escreva sua cidade: ")

rec = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=800075086904bb9b209a8f3bc28cd5d2')
tempo = json.loads(rec.text)

print('Condição do tempo: ',tempo['weather'][0]['main'])
temp = float(tempo['main']['temp']) - 273.15
print(f'temperatura: {temp:,.2f}Cº')