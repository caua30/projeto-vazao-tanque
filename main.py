# Criar uma classe Tanque em Python. Ela deve ter uma taxa de vazamento constante e um método para receber água da válvula.
import matplotlib

class Tanque:
    def __init__(self, capacidade_agua):
        self.capacidade_atual = capacidade_agua
        self.capacidade_maxima = 10000
        self.altura_agua = 1.0
        self.area_tanque = 1.0
        self.area_valvula = 0.0005
        self.volume_tanque = 1.0
        self.coeficiente_de_descarga = 0.62

    def receber_agua(self, quantidade_recebida):
        self.capacidade_atual += quantidade_recebida

    def taxa_vazamento(self):
        if self.altura_agua >= 0:
            self.vazamento = (self.coeficiente_de_descarga*self.area_valvula)*((2*9.81*self.altura_agua)**0.5)
            self.queda_agua = self.vazamento / self.area_tanque
            self.altura_agua = self.altura_agua - self.queda_agua
            self.capacidade_atual = self.capacidade_atual - self.vazamento
        else:
            self.capacidade_atual = 0 
            self.altura_agua = 0
         



meu_tanque = Tanque(2)
print("1,2,3,4")
while(meu_tanque.capacidade_atual >= 0.1):
    meu_tanque.taxa_vazamento()
    print(round(meu_tanque.altura_agua, 4))
    if meu_tanque.capacidade_atual < 0.1:
        print("o tanque foi esvaziado")
        break