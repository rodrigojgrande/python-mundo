#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
cont = 0
for c in range(1, 6):
    peso = float(input('Peso da \033[1;34m{}°\033[m pessoa: '.format(c)))
    
    if cont == 0:
        maior = peso
        menor = peso
        cont = 1
    else:
        if peso > maior:  
            maior = peso
        if peso < menor:  
            menor = peso
        
print('\033[1;32m{}\033[m é o maior e \033[1;31m{}\033[m é o menor peso'.format(maior, menor))