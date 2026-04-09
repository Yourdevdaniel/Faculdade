class Lescirc:
    def __init__(self, tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * tamanho
        self.inicio = 0
        self.fim = 0
        self.quant = 0
    def inserir_fim(self, valor):
        self.vetor[self.fim] = valor
        self.fim = (self.fim + 1) % self.tam_maximo
        self.quant+= 1
    def remover_fim(self):
        self.fim = (self.fim - 1) % self.tam_maximo
        self.quant -= 1
    def inserir_inicio(self, valor):
        self.inicio = (self.inicio - 1) % self.tam_maximo
        self.vetor[self.inicio] = valor
        self.quant += 1
    def remover_inicio(self):
        self.inicio = (self.inicio + 1) % self.tam_maximo
        self.quant -= 1
    def show(self):
        aux = self.inicio
        while aux!=self.fim:
            print(self.vetor[aux], end=' ')
            aux = (aux + 1) % self.tam_maximo
        print()
    def ver_primeiro(self):
        return self.vetor[self.inicio]
    def ver_ultimo(self):
        return self.vetor[(self.fim - 1) % self.tam_maximo]
