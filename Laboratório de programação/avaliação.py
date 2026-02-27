import random
# QUESTAO 1
lista = []
caractere = []
senha = []
removido = []
for i in range(6):
    lista.append(random.randint(0,9))
for i in range(3):
    cr = input("Digite um caractere especial de prerferencia: ")
    p = int(input("Digite a posição de onde ele devera ser inserido: "))
    caractere.append(cr)
    lista.insert(p,cr)
for i in range(len(lista)):
    senha.append(str(lista[i]))
print("====================================")
print("Caracteres que foi inserido na senha: ")
print(", ".join(caractere))
removido.append(senha[0])
senha.pop(0)
removido.append(senha[7])
senha.pop(7)
print("---------------")
print("Senha forte gerada: ")
print("".join(senha))
print("---------------")
print("Caracteres que foram removidos: ")
print(" ".join(removido))
print("====================================")

# QUESTAO 2
v = []
inv = []
inval = []
valid = []
for i in range(6):
    nome = input("Digite o nome do usuário: ")
    numero = nome.isalpha()
    if len(nome) < 5:
        inv.append(nome)
    elif numero is not True:
        inv.append(nome)
    else:
        v.append(nome)

for i in range(len(inv)):
    inval.append(inv[i].upper())


print("Nomes invalídos: ")
print(" ".join(inval))
v.sort()

print("Nomes Válidos: ")
for i in range(len(v)):
    print(f"{v[i]} quantidade de caracteres: {len(v[i])}")
    print("---------------------------------------------")




    
    