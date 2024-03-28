# Nqueen-backtracking
Problema das N rainhas utilizando backtracking

Backtracking é um algoritmo genérico que busca, por força bruta, soluções possíveis para problemas computacionais (tipicamente problemas de satisfações à restrições).

O problema das N-Rainhas é um dos desafios mais conhecidos na área de inteligência artificial e busca combinatória. Ele consiste em posicionar N rainhas em um tabuleiro de xadrez NxN de tal forma que nenhuma rainha ameace as outras, ou seja, nenhuma rainha pode estar na mesma linha, coluna ou diagonal de outra. 

Para avaliação do problema e das colisões são analisadas por um vetor s de n posições, em que cada célula Si representa a coluna j em que a rainha da linha i está posicionada, foi utilizado o problema formulado conforme visto na Equação da diagonal positiva e negativa com as características onde "i" é a linha e Si é a coluna. De maneira incremental, busca por candidatos à soluções e abandona cada candidato parcial C quando C não pode resultar em uma solução válida. Quando sua busca chega a uma extremidade da estrutura de dados, como um nó terminal de uma árvore, o algoritmo realiza um retrocesso tipicamente implementado através de uma recursão.
