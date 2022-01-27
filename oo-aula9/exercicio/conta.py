from cliente import Cliente

class Conta(Cliente):
    
    def __init__(self, nome ,cpf, idade, saldo, limite):
        Cliente.__init__(self, nome, cpf, idade)
        self.saldo = saldo
        self.limite = limite
    

    def sacar(self, sacar):
        if self.saldo - sacar <= 0:
            "Saldo Insuficiente"
        else:
            self.saldo -= sacar

    def depositar (self, depositar):
        self.saldo += depositar
    
    

    