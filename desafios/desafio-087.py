#Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
par = 0
maior = 0
soma = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
        
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
            
        if c == 2:
            soma += matriz[l][c]
        
        if l == 1 and c == 0:
            maior = matriz[l][c]
        else: 
            if l == 1:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]
        
    print()
print(f'A soma dos valores é de: {par}')
print(f'O maior valor da segunda linha é: {maior}')
print(f'A soma dos valores da terceira coluna é: {soma}')

#TEACHER WAY 
'''for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {soma}')

for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')'''