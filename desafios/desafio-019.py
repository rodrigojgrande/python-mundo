#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

primeiro = str (input('Primeiro aluno: '))
segundo = str (input('Segundo aluno: '))
terceiro = str (input('Terceiro aluno: '))
quarto = str (input('Quarto aluno: '))

lista = [primeiro, segundo, terceiro, quarto]

escolhido = choice(lista) 

print('O aluno escolhido foi {}'. format(escolhido))