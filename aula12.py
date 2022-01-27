# Bibliotecas, PIP e Requisiçoes web
#dois tipos de requisiçoes de web, get (pegar informaçoes), Post(Enviar informaçes)
import requests

requisicao = requests.get('https://solyd.com.br/')   #get, post, delete, outros(requisicoes web)
print(requisicao.text)

cabecalho = {'User-agent': 'Windows 12', 'Referer': 'https:// google.com'}
meus_cookies = {'Ultima-visita': '10-10-2021'}
dados = {'username':'Renan', 'password':'123'}
texto = None
try:
  requisicao1 = requests.post('https://putsreq.com/6zxaOAf0ndsAZja8OFMB', 
                              headers = cabecalho, cookies=meus_cookies,
                              data = dados)
  print(requisicao1.text)
except Exception as erro:
  print('Requisição deu erro, ', erro)
print(texto)