from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', 6, 'Ford', 120)

print(caminhao_rosa)

print(type(caminhao_rosa))

print('CAMINHAO ROSA')
print('Cor: ', caminhao_rosa.cor) 
print('Quantidade de rodas: ', caminhao_rosa.rodas)
print('Marca:  ',caminhao_rosa.marca)
print('Tanque: ',caminhao_rosa.tanque)

print("")

print("CARRO AZUL")
carro_azul = Carro('Azul','BMW', 10)

print('Cor: ', carro_azul.cor) 
print('Quantidade de rodas: ', carro_azul.rodas)
print('Marca:  ',carro_azul.marca)
print('Tanque: ',carro_azul.tanque)
carro_azul.abastecer(35)
print('Tanque: ',carro_azul.tanque)
carro_azul.abastecer(35)







