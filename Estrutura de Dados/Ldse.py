class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
        
class Ldse:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    def inserir_inicio(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor,None)
        else:
            self.prim = No(valor,None)
        self.quant += 1
    def inserir_fim(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor,None)
        else:
            self.ult.prox = self.ult = No(valor,None)
        self.quant += 1
    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end=" ")
            aux = aux.prox
        print("/n")
        """
        Outra forma 
        for i in range(self.quant):
            print(aux.info, end=" ")
        """
    def remover_fim(self):
        if self.quant == 1:
                self.prim = self.ult = None
        else:
            aux = self.prim
            while aux.prox != self.ult:
                aux = aux.prox
            aux.prox = None
            self.ult = aux
        self.quant -= 1
    """
    VERSÃO COM FOR
    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim
            for i in range(self.quant-2):
                aux = aux.prox
            aux.prox = None
            self.ult = aux
        self.quant -= 1 
    """
    def tamanho_atual(self):
        return self.quant
    def esta_vazia(self):
        return self.quant ==0
    def ver_primeiro(self):
        return self.prim.info
    def ver_ultimo(self):
        return self.ult.inf
    # fazer remover, buscar, inserir apos, inserir antes,
    