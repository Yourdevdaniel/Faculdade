def maior_temperatura(nome):
    nome_arquivo = str(nome + ".txt")
    with open(nome_arquivo, "r", encoding = "utf-8") as arquivo:
        conteudo = arquivo.readlines()
        lista = []
        lista_qt_maior = []
        for linha in conteudo:
            dados = linha.strip().split(";")
            temp = dados[1]
            temperatura = float(temp)
            lista.append(temperatura)
        for i in range(len(lista)):
            maiores = 0
            for j in range(len(lista)):
                if lista[i] < lista[j]:
                    for u in range(len(lista)):
                        if lista[u] > lista[i]:
                            maior = lista[u]
                            return print(maior)


                            
maior_temperatura("clima")
