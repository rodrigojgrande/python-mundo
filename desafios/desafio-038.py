#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))

if a > b:
    print('\033[1;33mO primeiro valor é maior.\033[m')
elif a < b:
    print('\033[1;34mO segundo valor é maior.\033[m')
elif a == b:
    print('\033[1;35mOs dois valores são iguais\033[m')
