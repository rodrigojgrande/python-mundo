#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
y = 0
z = 0
for c in range(1, 7):
    x = int (input('Digite o \033[1;34m{}°\033[m valor: '.format(c)))
    if x % 2 == 0:
        y += x
        z += 1
print('Você informou \033[1;33m{}\033[m valores pares e a soma deles é igual a \033[1;32m{}\033[m'.format(z, y))