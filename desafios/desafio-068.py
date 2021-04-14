#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

tentativas = 0

print('-=-' * 20)
print('\033[1;33mVAMOS JOGAR PAR OU ÍMPAR\033[m ')
print('-=-' * 20)

while True:
    machine = randint(0, 11)
    playerValue = int(input('\033[1;34mDigite um valor:\033[m '))
    playerEvenOdd = str(input('\033[1;34mPar ou Ímpar [P/I]:\033[m ').strip().upper()[0])
    
    print('\033[1;32mProcessando...\033[m')
    sleep(1)
    
    if playerEvenOdd not in 'PpIi':
        print('\033[1;31mCOMANDO INVÁLIDO\033[m')
        break
    
    soma = playerValue + machine 
    
    if soma % 2 == 0:
        result = 'Par'
    else:
        result = 'Impar'

    print(f'\033[1;33mVocê jogou {playerValue} e o computador {machine}. Total de {soma} deu {result}\033[m')
    #print('Deu Par' if soma % 2 == 0 else 'Deu Ímpar')

    result = result.strip().upper()[0]
    
    if result != playerEvenOdd:
        break
    
    tentativas += 1
    sleep(1)
    print('\033[1;33mVocê venceu!\033[m')
    sleep(1)
    print('\033[1;33mVamos jogar novamente...\033[m')
    
sleep(1)
print(f'\033[1;31mGame Over! Você venceu {tentativas} tentativas\033[m')