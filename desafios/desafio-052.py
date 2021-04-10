#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#Um número primo é aquele que é dividido apenas por um e por ele mesmo. 

valor = int (input('Valor : '))
cont = 0

for c in range(1, valor+1):

    if valor % c == 0:
        print('\033[1;33m', end='')
        cont +=1
    else:
        print('\033[1;31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(valor, cont))
if cont == 2:
    print('É primo!')
else:
    print('Não é primo!')