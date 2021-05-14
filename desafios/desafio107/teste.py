#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda #Importa tudo
#from moeda import metade, dobro, aumentar #importa métodos específicos
#import desafio-107.moeda #import através especificando a pasta
#from desafio-107 import moeda #importa especificando a pasta

p = float(input('Digite o preço R$'))
print(f'A Metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')