#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float (input('Qual é o salário do funcionário? R$'))
aumento = salario * 1.15
#aumento = salario + (salario * 15 / 100)

print('Um funcionário que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f}.'. format(salario, aumento))