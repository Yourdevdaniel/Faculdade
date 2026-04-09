class Les:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.vetor = [None] * tamanho
        self.quant = 0
    def inserir_fim(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1
    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end=' ')
        print()
    def remover_fim(self):
        self.quant -= 1
    def inserir_inicio(self, valor):
        for i in range(self.quant, 0, -1):
            self.vetor[i] = self.vetor[i - 1]
        self.vetor[0] = valor
        self.quant += 1
    def remover_inicio(self):
        for i in range(self.quant - 1):
            self.vetor[i] = self.vetor[i + 1]
        self.quant -= 1
    def remover_valor(self, valor):
        rem = -1
        for i in range(self.quant):
            if self.vetor[i] == valor:
                rem = i
                break
        if rem != -1:
            for i in range(rem, self.quant - 1):
                self.vetor[i] = self.vetor[i + 1]
            self.quant -= 1
    def get_prim(self):
        return self.vetor[0]
    def get_ult(self):
        return self.vetor[self.quant - 1]
    def get_capacidade(self):
        return self.tam
    def quantas_vagas(self):
        return self.tam - self.quant
    def remover(self, valor):
        n = -1
        for i in range(self.quant):
            if self.vetor[i] == valor:
                n = i
                break
        if n != -1:
            for i in range(n, self.quant - 1):
                self.vetor[i] = self.vetor[i + 1]
            self.quant -= 1
    def inserir_apos(self, valor1, valor2):
        num = -1
        for i in range(self.quant):
            if self.vetor[i] == valor2:
                num = i
                break
        if num != -1:
            for i in range(self.quant, num + 1, -1):
                self.vetor[i] = self.vetor[i - 1]
            self.vetor[num + 1] = valor1
            self.quant += 1
    def inserir_antes(self, valor1, valor2):
        num = -1
        for i in range(self.quant):
            if self.vetor[i] == valor2:
                num = i
                break
        if num != -1:
            for i in range(self.quant, num, -1):
                self.vetor[i] = self.vetor[i - 1]
            self.vetor[num] = valor1
            self.quant += 1
    def remover_anteriores(self, valor):
        val = -1
        for i in range(self.quant):
            if self.vetor[i] == valor:
                val = i
                break
        if val != -1:
            j = 0
            for i in range(val, self.quant):
                self.vetor[j] = self.vetor[i]
                j += 1
            self.quant -= val
    def remover_posteriores(self, valor):
        val = -1
        for i in range(self.quant):
            if self.vetor[i] == valor:
                val = i + 1
                break
        if val != -1:
            v = self.quant - val
            self.quant -= v
    def existe(self, valor):
        for i in range(self.quant):
            if self.vetor[i] == valor:
                return True
        return False
    def index(self, valor):
        val = -1
        for i in range(self.quant):
            if self.vetor[i] == valor:
                val = i
        return val
    def info(self, indice):
        if 0 <= indice < self.quant:
            return self.vetor[indice]
        return False
    def intervalo(self, posicao1, posicao2):
        qtd = posicao2 - posicao1 + 1
        j = posicao1
        for i in range(posicao2 + 1, self.quant):
            self.vetor[j] = self.vetor[i]
            j += 1
        self.quant -= qtd
    def show_reverso(self):
        for i in range(self.quant - 1, -1, -1):
            print(self.vetor[i], end=' ')
        print()
    def insere_ordenado(self, valor):
        for i in range(self.quant):
            if self.vetor[i] >= valor:
                break
        else:
            i = self.quant
        for j in range(self.quant, i, -1):
            self.vetor[j] = self.vetor[j - 1]
        self.vetor[i] = valor
        self.quant += 1