#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#a = int(input('Ano de nascimento: '))

print('Digite o dígito que corresponde ao seu sexo: ')
print('[ 1 ] MASCULINO: ')
print('[ 2 ] FEMININO: ')
sexo = int(input('Dígito: '))

if sexo == 1:
    from datetime import date

    date = date.today()
    anoAtual = date.year

    nascimento = int(input('Ano de nascimento: '))

    idade = anoAtual - nascimento
    if idade > 18:
        print('\033[1;34mQuem nasceu em {} tem {} anos em {}.\033[m'.format(nascimento, idade, anoAtual)) 
        print('\033[1;32mSeu alistamento foi há {} anos\033[m'.format(idade - 18))
        print('\033[1;32mSeu alistamento foi em {}\033[m'.format(nascimento + 18))
    elif idade < 18 and nascimento <= anoAtual:
        print('\033[1;34mQuem nasceu em {} tem {} anos em {}.\033[m'.format(nascimento, idade, anoAtual)) 
        print('\033[1;32mAinda faltam {} anos para o seu alistamento\033[m'.format(18 - idade))
        print('\033[1;33mSeu alistamento será em {}\033[m'.format(nascimento + 18))
    elif idade == 18:
        print('\033[1;34mQuem nasceu em {} tem {} anos em {}.\033[m'.format(nascimento, idade, anoAtual)) 
        print('\033[1;31mVocê deve se alistar imediatamente!\033[m')
    elif nascimento > anoAtual:
        print('\033[1;31mVocê nem nasceu ainda engraçadinho!\033[m')
if sexo == 2:
    print('\033[1;33mNão é necessário o alistamento militar obrigatório\033[m')
else: 
    print('\033[1;31mComando inválido\033[m')