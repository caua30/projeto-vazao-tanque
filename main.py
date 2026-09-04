# Criar uma classe Tanque em Python. Ela deve ter uma taxa de vazamento constante e um método para receber água da válvula.
import time
from abc import ABC, abstractmethod


class Tanque:
    def __init__(self, capacidade_agua=0, capacidade_maxima=10000):
        self.capacidade_atual = capacidade_agua
        self.capacidade_maxima = capacidade_maxima
        self.altura_agua = 1.0
        self.area_tanque = 1.0
        self.area_valvula = 0.0005
        self.volume_tanque = 1.0
        self.coeficiente_de_descarga = 0.62
        self.tempo_inicio = time.time()
        self.tempo_final = None
        self.delta_tempo = 0.0
        self.tempo_de_vazao = 0.0
        self.vazamento = 0.0
        self.queda_agua = 0.0

    def receber_agua(self, quantidade_recebida):
        self.capacidade_atual = min(self.capacidade_maxima, self.capacidade_atual + quantidade_recebida)
        self.altura_agua = max(0.0, min(self.altura_agua + (quantidade_recebida / self.area_tanque), 1.0))

    def taxa_vazamento(self):
        if self.altura_agua > 0:
            self.vazamento = (self.coeficiente_de_descarga * self.area_valvula) * ((2 * 9.81 * self.altura_agua) ** 0.5)
            self.queda_agua = self.vazamento / self.area_tanque
            self.altura_agua = max(0.0, self.altura_agua - self.queda_agua)
            self.capacidade_atual = max(0.0, self.capacidade_atual - self.vazamento)
        else:
            self.capacidade_atual = 0.0
            self.altura_agua = 0.0

    def tempo_vazao_total(self, nivel_alvo=0.0):
        return TempoFinal(self).calcular_tempo_total(nivel_alvo)


class TempoFinal(ABC):
    def __init__(self, tanque):
        self.tanque = tanque

    @abstractmethod
    def calcular_tempo_total(self, nivel_destino=0.0):
        """Calcula o tempo necessário para o nível da água atingir o valor desejado."""

    @abstractmethod
    def tempo_restante(self, nivel_destino=0.0):
        """Retorna o tempo restante para a vazão atingir o nível desejado."""


class TempoFinalTanque(TempoFinal):
    def calcular_tempo_total(self, nivel_destino=0.0):
        altura_inicial = max(0.0, self.tanque.altura_agua)
        nivel_destino = max(0.0, min(nivel_destino, altura_inicial))

        if altura_inicial <= nivel_destino:
            self.tanque.tempo_final = time.time()
            self.tanque.delta_tempo = 0.0
            self.tanque.tempo_de_vazao = 0.0
            return 0.0

        altura = altura_inicial
        tempo_total = 0.0
        passo_tempo = 0.1

        while altura > nivel_destino and altura > 0:
            vazamento = (self.tanque.coeficiente_de_descarga * self.tanque.area_valvula) * ((2 * 9.81 * altura) ** 0.5)
            queda = vazamento / self.tanque.area_tanque
            altura = max(0.0, altura - queda * passo_tempo)
            tempo_total += passo_tempo

        self.tanque.tempo_final = time.time()
        self.tanque.delta_tempo = tempo_total
        self.tanque.tempo_de_vazao = tempo_total
        return tempo_total

    def tempo_restante(self, nivel_destino=0.0):
        return self.calcular_tempo_total(nivel_destino)


# lembre de criar forma de pausar vazão e voltar e receber agua dentro do while
# lembre de calcular tempo de vazão também e de rever conceito do pq fazendo
# teste
meu_tanque = Tanque(0)
escolha = "0"

while escolha != "4":
    escolha = input("1 para vazar água até o nível escolhido\n2 para adicionar mais água ao tanque\n3 para ver quanta agua tem\n4 para encerrar\nEscolha: ")
    if escolha == "1":
        quantidade_vazao = float(input("Digite até que nível deseja que a água fique: "))
        tempo_estimado = TempoFinalTanque(meu_tanque).calcular_tempo_total(quantidade_vazao)
        print(f"Tempo estimado para atingir o nível desejado: {tempo_estimado:.2f} segundos")

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






