#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

date = date.today()
anoAtual = date.year

maior = 0
menor = 0

for c in range(1, 8):
    nascimento = int(input('Ano de nascimento da \033[1;34m{}°\033[m pessoa: '.format(c)))
    idade = anoAtual - nascimento
    
    if idade >= 18:  
        maior +=1
    else:
        menor +=1
    
print('\033[1;32m{}\033[m são maiores e \033[1;31m{}\033[m  são menores de idade'.format(maior, menor))