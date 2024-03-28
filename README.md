# Nqueen Problem

Português:

Problema das N rainhas utilizando backtracking

O problema das N-Rainhas é um dos desafios mais conhecidos na área de inteligência artificial e busca combinatória. Ele consiste em posicionar N rainhas em um tabuleiro de xadrez NxN de tal forma que nenhuma rainha ameace as outras, ou seja, nenhuma rainha pode estar na mesma linha, coluna ou diagonal de outra. 

Para avaliação do problema e das colisões são analisadas por um vetor s de n posições, em que cada célula Si representa a coluna j em que a rainha da linha i está posicionada, foi utilizado o problema formulado conforme visto na Equação da diagonal positiva e negativa com as características onde "i" é a linha e Si é a coluna. De maneira incremental, busca por candidatos à soluções e abandona cada candidato parcial C quando C não pode resultar em uma solução válida. Quando sua busca chega a uma extremidade da estrutura de dados, como um nó terminal de uma árvore, o algoritmo realiza um retrocesso tipicamente implementado através de uma recursão.

Backtracking é um algoritmo genérico que busca, por força bruta, soluções possíveis para problemas computacionais (tipicamente problemas de satisfações à restrições).

English:

N queens problem using backtracking

The N-Queens problem is one of the best-known challenges in the area of artificial intelligence and combinatorial search. It consists of positioning N queens on an NxN chessboard in such a way that no queen threatens the others, that is, no queen can be on the same line, column or diagonal as another.

To evaluate the problem and collisions are analyzed by a vector s of n positions, in which each cell Si represents the column j in which the queen of row i is positioned, the formulated problem was used as seen in the positive and negative diagonal equation with the characteristics where "i" is the row and Si is the column. Incrementally, it searches for candidate solutions and abandons each partial candidate C when C cannot result in a valid solution. When your search reaches an end of the data structure, such as a terminal node in a tree, the algorithm performs a backtracking typically implemented through a recursion.

Backtracking is a generic algorithm that searches, by brute force, possible solutions to computational problems (typically constraint satisfaction problems).
