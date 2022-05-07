'''
Desafio 03
Dado um vetor de números e um número n. Determine a soma com o menor número de elementos entre os números do vetor mais
próxima de n e também mostre os elementos que compõem a soma. Para criar a soma,
utilize qualquer elemento do vetor uma ou mais vezes.

Exemplo:

Entrada de dados:

N = 10
V = [2, 3, 4]

Saída de dados:

10
[2, 4, 4]
[3, 3, 4]

Explicação:

Se N = 10 e V = [2, 3, 4] você pode utilizar as seguintes soma: [2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 4, 4] ou [3, 3, 4].
 Como a quantidade de elementos em [2, 4, 4] e [3, 3, 4] é igual, os dois conjuntos devem ser mostrados.

'''
# Importa o módulo com a função para combinar
from itertools import combinations_with_replacement

# Realiza combinação do conjunto
comb = combinations_with_replacement([2, 3, 4], 3)

# Filtra as respotas solicitadas e exibe
for x in comb:
    if sum(x) == 10:
        print(f'\n  A menor combinação possivel com resultado da soma igual a 10 é: {x}')
