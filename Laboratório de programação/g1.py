leituras = [["Daniel", 32, 50],["Sheyla", 10, 20],["Ana", 40, 150],["Beto", 5, 20],["Kenia", 130, 200]]

def leitores_intensivos(lista):
    for i in range(len(lista)):
        if lista[i][2] > 40:
            print(lista[i])

def tempo_total_leitura(lista):
    soma = 0
    for i in range(len(lista)):
        numero = lista[i][1]
        soma += numero
    print(f"O tempo total de leitura é {soma}")

def velocidade_leitura(lista):
    listinha = []
    for i in range(len(lista)):
        a = lista[i][1]
        b = lista[i][2]
        resultado = a/b
        listinha.append((lista[i][0],resultado))
    print(listinha)
        
        

leitores_intensivos(leituras)
tempo_total_leitura(leituras)
velocidade_leitura(leituras)

#2
autorizados = ["FX123", "GH456","JK789"]

sessoes = [["Ainda estou aqui", 120],["De volta para o futuro",20], ["Capitão Jack Sparrow: A origem", 15],["Bolt: O super cão",80],]

def validar_acesso(codigo):
    if codigo[:1].isalpha() and codigo[2:].isnumeric():
        return True
    else:
        return False

def imprimir_sessoes(lista):
    for i in range(len(lista)):
        print(f"Sessão: {lista[i][0]} | Ingressos: {lista[i][1]}")


def lista_filmes(lista, valor):
    for i in range(len(lista)):
        if lista[i][1] <= valor:
            print(f"ALERTA: O filme {lista[i]} está com apenas {lista[i][1]} Ingressos")

def lista_organizada(lista):
    lista.sort()
    for i in range(len(lista)):
        print(f"Sessão: {lista[i][0]} | Ingressos: {lista[i][1]}")


codigo = input("Digite o codigo: ").strip().upper()
if validar_acesso(codigo):
    while True  :
        print("Oque deseja fazer? ")
        print("1 - Exibir todas as sessões")
        print("2 - Exibir sessão com valor minimo de ingressos")
        print("3 - Exibit nomes dos filmes em lista alfabetica")
        print("4 - Sair")
        op = int(input(" "))
        if op == 1:
            print("----------------------------")
            print("Lista de filmes:")
            imprimir_sessoes(sessoes)
            print("----------------------------")
        elif op == 2:
            v = int(input("Qual a quantidade de ingressos? "))
            lista_filmes(sessoes, v)
        elif op == 3:
            lista_organizada(sessoes)
        elif op == 4:
            print("saindo...")
            break
        
else:
    print("Codigo invalido porfavor tente novamente")


















