#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

#MY FAIL PROGRESS
'''num = [[], [], []]
temp = list()
valor = 0
for c in range(0, 3):
    num[0] = c
    for v in range(0, 3):
        valor = int(input(f'Digite o {v}° valor: '))
        num[1].append(valor)
        num[0].append(c)

print(f'Os valores pares digitados foram: {num[0]}')'''

#TEACHER WAY
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
    print()
