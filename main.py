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
         

#lembrar de criar forma de pausar vazão e voltar e receber agua dentro do while 
# teste
meu_tanque = Tanque(0)
escolha = "0"

while escolha != "4":
    escolha = input("1 para vazar água até o nível escolhido\n2 para adicionar mais água ao tanque\n3 para ver quanta agua tem\nEscolha: ")
    if escolha == "1":
        quantidade_vazao = float(input("Digite até que nível deseja que a água fique: "))
        while meu_tanque.altura_agua > quantidade_vazao:
            meu_tanque.taxa_vazamento()
            print(round(meu_tanque.altura_agua, 4))
        print("O tanque foi esvaziado até o nível escolhido")
    elif escolha == "2":
        quantidade_adicionada = float(input("Digite a quantidade de água a ser adicionada: "))
        meu_tanque.receber_agua(quantidade_adicionada)
    elif escolha == "3":
        print(meu_tanque.capacidade_atual)
    else:
        print("Opção inválida") 
        continue






