#Manipulação do arquivo
arquivo = open("A.txt", "r") #Abrindo arquivo 
verfiMat = []  
mat = [] 
verfiMat = arquivo.readlines() #Lê o arquivo e guarda os ves em uma variável 
arestaMult = 0
lacos = 0 

#Percorre a matriz e imprime os ves
print("MATRIZ DE ADJACÊNCIA DO GRAFO: ")
print("#---------------------------#")
print("")
for i in range(len(verfiMat)):
    mat.append(verfiMat[i].split()) 
for linha in verfiMat:   
    print(linha,end="") 
print("#---------------------------#")
print("")

#Verifica se há arestas múltiplas e se houver imprime-as
contAresMult = 0
print("HÁ ARESTAS MÚLTIPLAS E LAÇOS NO GRAFO? SE HOUVER MOSTRE EM QUAIS VÉRTICES ELES SE ENCONTRAM.\n")
print("#---------------------------#")
print("")
for linha in verfiMat:     
    if '2' in linha : #Se houver um 2 na linha, significa que há arestas múltiplas
        print("Na linha {} há uma aresta multipla\n".format(contAresMult+1))
        arestaMult = arestaMult + 1
    contAresMult = contAresMult +1 #Faz a contagem de arestas múltiplas do grafo

#Verifica se há laços e se houver imprime-os
verifiCol = 0
verifiLin = 0
for linha in mat:
    for i in range(len(linha)):
        if linha[verifiCol] == "1": #Se houver 1 no mesmo indice da linha e da coluna, significa que há laco
            print("Há um laço na linha {} coluna {}\n".format(verifiLin+1, verifiCol+1))
            lacos = lacos + 1 #Guarda a quantidade de laços em uma variável
        verifiLin = verifiLin + 1 
        verifiCol = verifiCol + 1   
        break
print("#---------------------------#")


arquivo = open('A.txt', 'r') #Abre o arquivo 
verfiMat = []  
mat = [] 
verfiMat = arquivo.readlines() #Lê o arquivo e guarda os ves em uma variável
arquivo.close() #Salva e fecha o arquivo
finalMat = []

for m in verfiMat: #Entra no loop para cada linha da matriz e remove as quebras de linha
    m = m.rstrip('\n')
    finalMat.append(m)
for num in finalMat:
    if '' in finalMat:
        finalMat.remove('') #Remove os espaços em branco

matOne=[[int(num) for num in line.split(' ')] for line in finalMat] #Transforma a lista em uma matriz
matSnd = [[int(num) for num in line.split(' ')] for line in finalMat] #Cria uma segunda matriz igual a primeira para facilitar a manipulação

#Verifica o grau de cada vértice da matriz e ordena-os em ordem decrescente
seqGrau = []

for linha in range(len(matSnd)):
    for verifiCol in range(len(matSnd[linha])):
        if verifiCol == linha and matSnd[linha][verifiCol]>= 1:
            matSnd[linha][verifiCol] = matSnd[linha][verifiCol]*2
for linha in matSnd:
    seqGrau.append(sum(linha))

seqGrau.sort(reverse=True) #Muda a ordem dos graus para decrescente
print("")
print("QUAL A SEQUÊNCIA DOS GRAUS DO GRAFO?")
print("")
print("#---------------------------#")
print("")
print("Sequência de graus do grafo = {}".format(seqGrau))
print("")
print("#---------------------------#")
print("")    

#Verifica a quantidade de arestas da matriz
contAre = 0

for linha in range(len(matSnd)): #Conta o número de arestas
    for verifiCol in range(len(matSnd[linha])):
        contAre = contAre + matSnd[linha][verifiCol]

print("QUAL O NÚMERO DE ARESTAS DO GRAFO?")
print("")
print("#---------------------------#") 
print("")
print("O grafo possui {} arestas\n".format(int(contAre/2)))
print("#---------------------------#")
print("")    


#Verifica se o grafo possui laços ou arestas múltiplas para facilitar a função de grafo completo
verifiAresMult = 0
verifiLacos = 0

for linha in range(len(matOne)):
    for verifiCol in range(len(matOne[linha])):
        if linha == verifiCol and matOne[linha][verifiCol] > 0:
            verifiLacos = verifiLacos + matOne[linha][verifiCol]
        if matOne[linha][verifiCol] > 1 and linha != verifiCol:
            verifiAresMult = verifiAresMult + 1

print("O GRAFO É COMPLETO?\n")
print("#---------------------------#\n")
#Verifica se o grafo é completo
if verifiLacos > 0 or verifiAresMult > 1:
    print("O grafo não é completo!\n")
elif verifiLacos == 0 and verifiAresMult == 0:
    verifica = 0
    bef = 0
    aft = 0
    for m in seqGrau:
        aft = m
        if m == bef:
            verifica = 1
        else:
            bef = aft
            verifica = 0
    if verifica == 0:
        print("O grafo não é completo!\n")
    elif verifica == 1:
        print("O grafo é completo!\n")

print("#---------------------------#") 
print("")         

print("O GRAFO É REGULAR?\n")
print("#---------------------------#\n")    
#Verifica se o grafo é regular
verifica2 = 0
bef = 0
aft = 0
for m in seqGrau:
    aft = m
    if m == bef:
        verifica2 = 1
    else:
        bef = aft
        verifica2 = 0
if verifica2 == 0:
    print("O grafo não é regular!\n")
elif verifica2 == 1:
    print("O grafo é regular!\n")


arquivo = open('A.txt', 'r') #Lê o arquivo
text = arquivo.readlines() 
mat =[]
for i in text:
    i = i.rstrip('\n') #Remove a quebra de linha    
    mat.append(i)
for v in mat:
    if '' in mat:
        mat.remove('') #Remove os espaços em branco
matOne=[[int(v) for v in linha.split(' ')] for linha in mat]
arquivo.close()

#Função para verificar se o grafo é bipartido
def biPart(graph):
    v = 0
    verticeU =[]
    verticeV =[]

    def side(y):
        if len(verticeV) > 1:
            for i in range(len(verticeV)):
                for j in range(len(verticeV)):
                    m = verticeV[i]
                    f = verticeV[j]
                    if graph[m][f] != 0:
                        return True
        return False

    for i in range(len(graph)):
        if i not in verticeV:
            verticeU.append(i)
            for j in range(len(graph)):
                if j > i:
                    if graph[i][j] > 0:
                        if j not in verticeV:
                            verticeV.append(j)
        if side(verticeV):
            bipart = False
        else:
          bipart = True


    if bipart:
        v+=("É um grafo bipartido pois os vértices podem ser divididos em dois conjuntos U e V, onde os vértices do conjunto U só podem se ligar aos vértices do conjunto V.\n")
        for i in range(len(verticeU)):
            if i < len(verticeU)-1:
                v+=("U{}".format(verticeU[i]+1) + ", ")
            else:
                v+=("U{}".format(verticeU[i]+1)+ "} e ")

        for j in range(len(verticeV)):
            if j < len(verticeV)-1:
                v+=("V{}".format(verticeV[j] + 1) +", ")
            else:
                v+=("V{}".format(verticeV[j] + 1) + "}")
        v+=("\n")
        
#Essa função verifica se é bipartido completo
        def bipartComp(u, v, matriz):
            result = ""

            for i in range(len(u)):
                count = 0
                for j in range(len(v)):
                    k = u[i]
                    z = v[j]
                    if matriz[k][z] > 0:
                        count+=1
                if count < len(v):
                    compara = False
                    break
                else:
                  compara = True
                  break


            if compara:
                result+=("O grafo é bipartido completo pois todos os vértices de um conjunto se liga a todos os outros vértices do outro conjunto.\n")
            else:
                result+=("O grafo não é bipartido completo pois nem todos vértice do primeiro conjunto está conectado a cada vértice do segundo conjunto.\n")
            return result

        v+= bipartComp(verticeU, verticeV, graph)
        return v

    else:
        return("O grafo não é bipartido porque os vértices não podem ser divididos em dois conjuntos U e V, ou seja, dois ou mais vértices se conectam no mesmo conjunto.\n")
print("#---------------------------#\n")
print("O GRAFO É BIPARTIDO? CASO SEJA, ELE É COMPLETO? SE FOR APRESENTE A BIPARTIÇÃO.\n")
print("#---------------------------#\n")
print(biPart(matOne))
print("#---------------------------#")         