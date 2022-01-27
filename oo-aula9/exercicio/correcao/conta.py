from cliente import Cliente

class Conta(Cliente):
    
    def __init__(self, cliente, saldo, limite):
        
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0-limite
    

    def sacar(self, sacar):
        if self.saldo - sacar < self.limite:
            "Saldo Insuficiente"
        else:
            self.saldo -= sacar

    def depositar (self, depositar):
        if depositar > 0:
            self.saldo += depositar
            print('Deposito realizado com sucesso, seu saldo agora é :', self.saldo)
        else:
            print("Erro de depósito")
    
    def consulta_saldo(self):
        return self.saldo
        
    
    

    