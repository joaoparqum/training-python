#underline na frente do atributo representa privado

class Conta:

    def __init__(self, agencia, saldo = 0):
        self._saldo = saldo
        self.agencia = agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo
        
conta = Conta("0001",500)
conta.depositar(200)
conta.sacar(100)

print(conta.agencia)
conta.mostrar_saldo()



