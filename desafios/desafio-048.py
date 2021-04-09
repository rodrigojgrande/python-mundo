#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

x = 0
n = 0
for c in range(3, 500, 3):
    if c % 2 != 0: 
        x = x + c 
        n = n + 1
    print(c)
print(x)
print(n)

#Teacher Way
soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos ps {} valores solicitados é {}'.format(cont, soma))