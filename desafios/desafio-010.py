#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float (input('Quanto dinheiro você têm na sua carteira?: R$'))
dolar = 5.75
cambio = real / dolar
print('Com R${} você pode comprar US${:.4}'. format(real, cambio))