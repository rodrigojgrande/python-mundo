#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

x = int(input('\033[1;34mPrimeiro Valor?\033[m '))
y = int(input('\033[1;34mSegundo Valor?\033[m '))

while sair != True:
    print('[ \033[1;33m1\033[m ] Somar')
    print('[ \033[1;33m2\033[m ] Multiplicador')
    print('[ \033[1;33m3\033[m ] Maior')
    print('[ \033[1;33m4\033[m ] Novos números')
    print('[ \033[1;33m5\033[m ] Sair do programa')
    
    opcao = int(input('\033[1;34mQual a sua opção?\033[m '))
    if opcao == 1:
        print('{} + {} = \033[1;32m{}\033[m '.format(x, y, x+y))
    elif opcao == 2:
        print('{} x {} = \033[1;32m{}\033[m '.format(x, y, x*y))
    elif opcao == 3:
        if x > y:
            print('\033[1;32m{}\033[m  é maior'.format(x))
        elif x < y:
            print('\033[1;32m{}\033[m  é maior'.format(y))
        else:
            print('\033[1;32m{}\033[m é igual a \033[1;32m{}\033[m '.format(x, y))
    elif opcao == 4:
        x = int(input('\033[1;34mPrimeiro Valor?\033[m '))
        y = int(input('\033[1;34mSegundo Valor?\033[m '))
    elif opcao == 5:
        sair = True
    else:
        print('Opção inválida! Tente novamente!')
print('\033[1;32mFinalizando...\033[m')
sleep(1)
print('\033[1;32mFim do programa! Volte sempre!\033[m')
