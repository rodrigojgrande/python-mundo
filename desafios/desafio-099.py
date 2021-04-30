#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* num):
    m = x = c = 0
    for valor in num:
        if x == 0:
            m = valor
            x += 1
        else:
            if valor > m:
                m = valor
        c += 1
    print(f'Foram passados {c} ao todo')
    print(f'O maior valor informado foi {m}')


maior()

