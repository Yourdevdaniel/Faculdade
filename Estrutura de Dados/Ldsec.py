class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
class Ldsecirc:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
            self.ult.prox = self.prim
        else:
            self.prim = No(valor, self.prim)
            self.ult.prox = self.prim
        self.quant += 1

    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.ult.prox = self.prim
        self.quant -= 1

    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
            self.ult.prox = self.prim
        else:
            self.ult.prox = No(valor, None)
            self.ult = self.ult.prox
            self.ult.prox = self.prim
        self.quant += 1

    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim
            while aux.prox != self.ult:
                aux = aux.prox
            aux.prox = self.ult.prox
            self.ult = aux
        self.quant -= 1

    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(aux.info, end=" ")
            aux = aux.prox
        print("\n")

    def estaVazia(self):
        return self.quant == 0

    def tamanho_atual(self):
        return self.quant

    def ver_primeiro(self):
        return self.prim.info

    def ver_ultimo(self):
        return self.ult.info
