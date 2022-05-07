'''
Desafio 01
Alguns números inteiros positivos n possuem uma propriedade na qual a soma de n + reverso(n) resultam em números ímpares.
Por exemplo, 36 + 63 = 99 e 409 + 904 = 1313. Considere que n ou reverso(n) não podem começar com 0.

Existem 120 números reversíveis abaixo de 1000.

Construa um algoritmo que mostre na tela todos os números n onde a soma de n + reverso(n)
resultem em números ímpares que estão abaixo de 1 milhão.
'''


#função para inverter numero
def inverter(numero):
    inverso = 0
    while (numero != 0):
        temp = numero % 10
        inverso = inverso * 10 + temp
        numero = numero // 10
    return inverso

# Variaveis
x = 1
resultado = []

# Realiza soma de N + reverso(n)
for numero in range(1000000):
    inverso = inverter(numero)
    soma = numero + inverso
    # Filtra numeros com soma abaixo de 1kk, retira numeros começando com 0, filtra n + reverso(n) igual a numero impar
    if soma % 2 != 0 and soma < 1000000 and numero % 10 != 0:
        resultado.append(numero)
        x += 1
# Exibe resultado
print(resultado)
print(f'\nExistem {len(resultado)} numeros com n + reverso(n) resultando'
                f' em números ímpares que estão abaixo de 1 milhão.')
