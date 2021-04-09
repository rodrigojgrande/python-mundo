#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

x = int (input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    print('{} X {:2} = {:2}'. format(x, c, x*c))