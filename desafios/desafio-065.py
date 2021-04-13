#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resposta = 'Ss'
total = c = media = 0

while resposta in 'Ss':
    n = int (input('Digite um número: '))
    total += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resposta = str (input('Quer continuar? [S/N] ').upper().strip()[0])
media = total / c
print('Você digitou {} números e a média foi {}'.format(c, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
