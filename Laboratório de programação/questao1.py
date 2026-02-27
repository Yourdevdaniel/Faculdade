cidades = ["CidadeA", "CidadeB","CidadeC",'CidadeD']
temp = [28.5,34.0,27.8,31.0]
cont = -1 #usei todo minha cabeça nesse -1

with open("clima.txt", "w", encoding = "utf-8") as arquivo:
        for temperatura in temp:
            cont = cont + 1
            temperatura_final = str(temperatura)
            cidade = cidades[cont]
            arquivo.write(cidade + ";" + temperatura_final+"\n")


