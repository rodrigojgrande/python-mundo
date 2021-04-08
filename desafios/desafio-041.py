#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date

date = date.today()
anoAtual = date.year
nascimento = int(input('Ano de nascimento: '))
idade = anoAtual - nascimento

if nascimento > anoAtual:
    print('\033[1;31mAtleta ainda não nasceu!\033[m')
else:
    print('o Atleta têm \033[1;34m{}\033[m anos'.format(idade))
    if idade <= 9:
        print('Classificação: \033[1;33mMIRIM\033[m')
    elif idade < 9 and idade <= 14:
        print('Classificação: \033[1;33mINFANTIL\033[m')
    elif idade < 14 and idade <= 19:
        print('Classificação: \033[1;33mJÚNIOR\033[m')
    elif idade < 19 and idade <= 25:
        print('Classificação: \033[1;33mSÊNIOR\033[m')
    elif idade < 25:
        print('Classificação: \033[1;33mMASTER\033[m')
    else:
        print('\033[1;31opsss! Algo de inesperado aconteceu!\033[m')
