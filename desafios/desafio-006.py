#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

x = int (input('Digite um número: '))
print('Analisando o valor {}, seu dobro é {}, o triplo é {} e a raiz quadrada é {}'. format(x, (x*2), (x*3), (x**(1/2))))