figuras_para_teste = [[5.0,5.0], [4.0,7.0],[3.0,2.0]]
def quadrado(lista):
    for i in range(len(lista)):
        j = lista[i][1]
        if lista[i] == j:
            print("verdade")
        else:
            print("False")
        

print(quadrado(figuras_para_teste))                  
        

def calcula_area(largura,altura):
    return largura * altura

for i in figuras_para_teste:
    for j in range(2):
        print(calcula_area(i,j))
    













    #def calcula_area(largura,altura):
    #return largura * altura
    
