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
        # lembrar de atualizar variaveis de area para ser atualizada a cada iteração
        self.vazamento = (self.coeficiente_de_descarga*self.area_valvula)*((2*9.81*self.altura_agua)**0.5)
        self.altura_agua = self.altura_agua - self.vazamento
        self.capacidade_atual = self.capacidade_atual - self.vazamento



meu_tanque = Tanque(1000)
print("1,2,3,4")
while(meu_tanque.capacidade_atual != 0):
    meu_tanque.taxa_vazamento()
    print(meu_tanque.capacidade_atual)