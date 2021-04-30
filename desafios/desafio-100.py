#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
def somaPar(sorteados):
    total = 0
    for c, v in enumerate(sorteados):
        if v % 2 == 0:
            total += v
        print(f'O {c+1}° valor foi {v}')
    print(f'A soma dos pares é {total}!')
    
    
def sorteia():
    sorteados = list()
    for c in range(1, 6):
        sorteados.append(randint(1, 11))

    somaPar(sorteados)

sorteia()
