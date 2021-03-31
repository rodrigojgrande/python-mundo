#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input('Qual a distância da sua viagem? '))

viagem = 200

valorCurta = 0.50
valorLonga = 0.45

if distancia > viagem:
    total = (distancia * valorLonga) 
    print('Você está prestes a começar uma viagem de {:.0f}Km.'.format(distancia))
    print('E o preço da sua passagem será de R${:.2f}'.format(total))
else: 
    total = (distancia * valorCurta) 
    print('Você está prestes a começar uma viagem de {:.0f}Km.'.format(distancia))
    print('E o preço da sua passagem será de R${:.2f}!'.format(total))