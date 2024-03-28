# Nqueen + Backtracking

Português:

Problema das N rainhas utilizando backtracking

O problema das N-Rainhas é um dos desafios mais conhecidos na área de inteligência artificial e busca combinatória. Ele consiste em posicionar N rainhas em um tabuleiro de xadrez NxN de tal forma que nenhuma rainha ameace as outras, ou seja, nenhuma rainha pode estar na mesma linha, coluna ou diagonal de outra. 

Na implementação do backtracking para resolver o problema das N Rainhas, eu iterei as colunas do tabuleiro e coloquei uma rainha em cada coluna e, em seguida, verificando se ela pode ser colocada sem atacar as outras rainhas já posicionadas. Se uma posição válida for encontrada, a recursão continua para a próxima coluna. Se em algum momento não for possível colocar uma rainha sem que ela ataque as outras, o algoritmo recua para a coluna anterior (backtracking) e tenta outra posição. Esse processo continua até que todas as colunas tenham sido preenchidas, resultando em uma solução válida, ou até que todas as possibilidades tenham sido testadas sem sucesso.

Backtracking é um algoritmo genérico que busca, por força bruta, soluções possíveis para problemas computacionais (tipicamente problemas de satisfações à restrições).

English:

N queens problem using backtracking

The N-Queens problem is one of the best-known challenges in the area of artificial intelligence and combinatorial search. It consists of positioning N queens on an NxN chessboard in such a way that no queen threatens the others, that is, no queen can be on the same line, column or diagonal as another.

In implementing backtracking to solve the N Queens problem, I iterated over the columns of the board and placed a queen in each column and then checking if it can be placed without attacking the other queens already placed. If a valid position is found, the recursion continues to the next column. If at any point it is not possible to place a queen without it attacking the others, the algorithm moves back to the previous column (backtracking) and tries another position. This process continues until all columns have been filled, resulting in a valid solution, or until all possibilities have been tested without success.

Backtracking is a generic algorithm that searches, by brute force, possible solutions to computational problems (typically constraint satisfaction problems).
