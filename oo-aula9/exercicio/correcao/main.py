from cliente import Cliente
from conta import Conta


cliente1 = Cliente("Renan", "123.456.789-10", 20)

conta_renan = Conta(cliente1, 100, 1000)







print("O que deseja fazer?\n1 : sacar\n2 : Depositar \n3 : Ver saldo \n4 : Sair")
operacao = int(input())
loop = True
while operacao < 1 or operacao >4:
    print("Operacao não identificada, digite outra \n1 : sacar\n2 : Depositar \n3 : Ver saldo \n4 : Sair")
    operacao = int(input())
    

while loop:

    if operacao == 1:
        conta_renan.sacar(int(input("Quanto voce deseja sacar? ")))
        print('Saque realizado com sucesso, seu saldo agora é :', conta_renan.consulta_saldo())
        
        
    
    if operacao == 2:
        conta_renan.depositar(int(input("Digite o valor do depósito: ")))
        

    if operacao == 3:
        print("Seu saldo é de: ", conta_renan.consulta_saldo())
    
    if operacao <1 or operacao > 4:
        print("Operacao não identificada, digite outra")

    
    print("\nO que deseja fazer?\n1 : sacar\n2 : Depositar \n3 : Ver saldo \n4 : Sair")
    operacao = int(input())

    if operacao == 4:
        print("Operação encerrada.")
        loop = False

    
        





    


