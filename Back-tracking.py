N = int(input("Insira o valor de N: "))
'O usuario deve inserir a quantidade de rainhas'
tabuleiro = [[0 for i in range(N)]for i in range(N)]
'Foi montada uma matriz que simula o tabuleiro'
'----------------------------------------------------------------------------------'
'A seguir montei uma função para checar o valor da rainha, ou seja,'
'se rainha está presente no nível da linha anterior ou não'
def checar_coluna (tabueiro,linha,coluna):
    for i in range(linha,-1,-1):
        if tabuleiro[i][coluna]==1:
            return False
    'Se a chamada for iterada sobre a função retorna true'
    return True

'Vamos supor que a rainha está posicionada em uma casa, então eu checo para essa coluna'
'se isso é um shape ou não, depois vejo em qual coluna está posicionada'
'esse é o motivo pelo qual eu coloco a coordenada'
'----------------------------------------------------------------------------------'

'Função para checar a diagonal da rainha, ou seja as duas diagonais possíveis'

def checar_diagonal (tabuleiro,linha,coluna):
    'A seguir será feita a lógica para a diagonal superior esquerda'
    for i,j in zip(range(linha,-1,-1),range(coluna,-1,-1)): 
        'A seguir coloquei que se for igual a 1 significa que a rainha esta presente'
        'na diagonal, ou seja o resultado é falso'
        if tabuleiro[i][j]==1:
            return False
    'A seguir eu chequei a diagonal superior direita'
    for i,j in zip(range(linha,-1,-1),range(coluna,N)):
        if tabuleiro[i][j]==1:
            return False
    'Se passar nesses dois testes de loop ela retorna verdadeira'
    return True

'-----------------------------------------------------------------------------------'

#backtracking
'A seguir defini a main da rainha'
def Nqueen(tabuleiro,linha):
    if linha==N:
        return True
    'E o teste final foi feito, pois se for verdade a posição da rainha será checada'
    'e retornará na posição correta se a checagem da diagonal e da coluna estiverem corretas.'
    'Ou seja, realizei isso para checar se esse local é o shape ou não'
    for i in range(N):
        if(checar_coluna(tabuleiro,linha,i)==True and checar_diagonal(tabuleiro,linha,i)==True):
            tabuleiro[linha][i]=1
            if Nqueen(tabuleiro,linha+1):
                return True
            tabuleiro[linha][i]=0
    return False
'Esse tabuleiro linha 0 condiz que não seja uma posição segura para a rainha'
'pois após a checagem não condiz com o resultado e é colocado o 0'
    
Nqueen(tabuleiro,0)

for linha in tabuleiro:
    print(linha)