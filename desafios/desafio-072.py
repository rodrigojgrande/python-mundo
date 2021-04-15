#Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

#ME IF
x = int(input('\033[1;34mDigite um número entre 0 e 20:\033[m '))
if x <= 0 or x >= 20:
    print('Valor inválido')
else:
    print(f'Você digitou o número {tupla[x]}')

#TEACHER WHILE
while True:
    x = int(input('\033[1;34mDigite um número entre 0 e 20:\033[m '))
    if 0 <= x <= 20:
        break
    print('Valor inválido. Tente novamente')
print(f'Você digitou o número {tupla[x]}')