#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

#CÁLCULO APENAS COM MATEMÁTICA 

#hipotenusa² = cateto oposto² + cateto adjacente²
#(**(1/2) = Raiz Quadrada

co = float (input('Comprimento do cateto oposto: '))
ca = float (input('Comprimento do cateto adjacente: '))
hi = (ca ** 2 + co ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'. format(hi))


#CÁLCULO APENAS COM MÓDULO 

from math import hypot
co = float (input('Comprimento do cateto oposto: '))
ca = float (input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'. format(hi))