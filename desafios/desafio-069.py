#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

y = 0
x = 0

idade = 0
homens = 0
maiores = 0
novinhas = 0

while True:
    print('-'*30)
    print('---- \033[1;34mCadastre uma pessoa\033[m ----')
    print('-'*30)
    idade = int(input('Idade: '))
    
    if idade < 0 or idade > 115:
        print('\033[1;31mCOMANDO INVÁLIDO\033[m')
        break
    
    sexo = str(input('Sexo [M/F]: ').strip().upper()[0])
    
    if sexo not in 'MmFf':
        print('\033[1;31mCOMANDO INVÁLIDO\033[m')
        break
    
    if idade > 18:
        maiores += 1
    
    if sexo == 'M':
        homens += 1
    
    if sexo == 'F' and idade < 20:
        novinhas += 1
        
    again = str(input('\033[1;33mQuer continuar [S/N]:\033[m ').strip().upper()[0])
    
    if again == 'N':
        break
    
print('Total de pessoas com mais de 18 anos: \033[1;32m{}\033[m '.format(maiores))
print('Ao todo temos \033[1;32m{}\033[m cadastrados'.format(homens))
print('E temos \033[1;32m{}\033[m mulheres com menos de 20 anos'.format(novinhas))
