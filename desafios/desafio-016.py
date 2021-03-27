#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
#from math import trunc

value = float (input('Digite um valor: '))
inter = math.trunc(value)

print('O valor digitado foi {} e a sua porção inteira é {}'. format(value, inter))
#print('O valor digitado foi {} e a sua porção inteira é {}'. format(value, int(num)))