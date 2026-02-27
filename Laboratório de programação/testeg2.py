with open ("produtos.txt","r",
           encoding="utf-8") as arquivo:
    produtos = {}
    for linha in arquivo.readlines():
        nome,quantidade = linha.strip().split(",")
        qtd = int(quantidade)
        produtos[nome] = qtd
        
with open ("precos.txt","r",
          encoding="utf-8") as arquivo:
    precos = {}
    for linha in arquivo.readlines():
        nome,valor = linha.strip().split(";")
        preco = float(valor)
        precos[nome] = preco


#while True:
    Quantidade = []
    Valores = []
    valor_final = []
    final = []
    lista = []
    nomes = []
    with open ("precos.txt","r",
          encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            nome,valor = linha.strip().split(";")
            preco = float(valor)
            Valores.append(preco)
    with open ("produtos.txt","r",
           encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            nome,quantidade = linha.strip().split(",")
            qtd = float(quantidade)
            Quantidade.append(qtd)
    with open ("precos.txt","r",
          encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            nome,valor = linha.strip().split(";")
            nomes.append(nome)
            

    for preco in range(len(Quantidade)):
        preco_final = Quantidade[preco] * Valores[preco]
        valor_final.append(preco_final)



    

print(nomes)
print(valor_final)
