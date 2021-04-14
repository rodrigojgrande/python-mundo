#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    x = int (input('Quer ver a tabuada de qual valor? '))
    if x < 0:
        break
    for c in range(1, 11):
        print('{} X {:2} = {:2}'. format(x, c, x*c))
print('Programa encerrado')