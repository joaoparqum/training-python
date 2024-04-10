from abc import ABC, abstractmethod

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTv(ControleRemoto):

    def ligar(self):
        print("ligando tv")

    def desligar(self):
        print("desligando tv")

controle = ControleTv()
controle.ligar()
controle.desligar()