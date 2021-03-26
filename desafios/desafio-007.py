#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
x = float (input('Digite a primeira nota: '))
y = float (input('Digite a segunda nota: '))
media = (x+y)/2
print('Primeira nota: {:.1f}\nSegunda nota: {:.1f} \nMédia: {:.1f}'. format(x, y, media))