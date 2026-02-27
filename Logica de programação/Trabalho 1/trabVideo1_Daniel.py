
# Você deve fazer um programa que leia 5 números reais e:

# a) calcule e apresente a soma dos números pares;

# b) para cada número, imprima uma mensagem dizendo a qual dos seguintes intervalos o número
# pertence: [0,25] (25,50], (50,75], (75,100]. Se o número digitado for menor que zero ou maior
# que 100, o programa deverá imprimir a mensagem “Fora de intervalo”

pergunta = 1
soma = 0

while pergunta <=5:
    numero = float(input("Digite um numero real: "))

    if numero % 2 == 0:
        soma += numero
    
    if 0 <= numero <= 25:
        print("Intervalo [0,25]")
    elif 25 < numero <= 50:
        print("Intervalo (25,50]")
    elif 50 < numero <= 75:
        print("Intervalo (50,75]")
    elif 75 < numero <= 100:
        print("Intervalo (75,100]")
    else:
        print("Fora de intervalo")

    pergunta += 1
print(f"Soma dos números pares: {soma}")
