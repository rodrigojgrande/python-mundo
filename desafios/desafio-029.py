#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')

velocidade = int(input('Qual a velocidade atual do seu carro? '))

limite = 80

if velocidade > limite:
    multa = (velocidade - limite) * 7
    print('MULTADO! Você excedeu o limite permitido que é de {}Km/h'.format(velocidade))
    print('Você deve pagar uma multa de R${},00!'.format(multa))
else: 
    print('Tenha um bom dia! Dirija com segurança!')