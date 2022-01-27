from cliente import Cliente
from conta import Conta


cliente1 = Conta("Renan", "123.456.789-1", 20, 1000, 1500)

print("O que deseja fazer?\n1 : sacar\n2 : Depositar \n3 :  Ver saldo")
operacao = int(input())

while operacao == 0 or operacao > 3:
    print('Selecione uma operação: \n1 : sacar\n2 : Depositar \n3 : Ver saldo')
    operacao = int(input())

if operacao == 1:
    cliente1.sacar(int(input("Quanto voce deseja sacar? ")))
    print('Saque realizado com sucesso, seu saldo agora é :', cliente1.saldo)
    operacao = 0

if operacao == 2:
    cliente1.depositar(int(input("Digite o valor do depósito: ")))
    print('Deposito realizado com sucesso, seu saldo agora é :', cliente1.saldo)
    operacao = 0
if operacao == 3:
    print("Seu saldo é de: ", cliente1.saldo)





    


