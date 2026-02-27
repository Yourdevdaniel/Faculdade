dicionario = {}

with open("clima.txt", "r", encoding = "utf-8") as arquivo:
    conteudo = arquivo.readlines()
    for linha in conteudo:
        dados = linha.replace("\n", "").split(";")
        nome = dados[0]
        temperatura = dados[1]
        temp = float(temperatura)
        dicionario[nome] = temp


print(dicionario)
        
