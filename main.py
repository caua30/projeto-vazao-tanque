# Criar uma classe Tanque em Python. Ela deve ter uma taxa de vazamento constante e um método para receber água da válvula.

class Tanque:
    def __init__(self, capacidade_agua):
        self.capacidade_atual = capacidade_agua
        self.capacidade_maxima = 10000

    def receber_agua(self, quantidade_recebida):
        self.capacidade_atual += quantidade_recebida

    def taxa_vazamento(self,pressão_final , pressão_inicial, volume, tempo):
        self.vazamento = (pressão_final - pressão_inicial)*volume/tempo
        self.capacidade_atual = self.capacidade_atual - self.vazamento

