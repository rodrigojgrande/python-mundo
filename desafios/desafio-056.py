#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

y = 0
x = 0
idade = 0
media = 0
velho = 0
novinha = 0
mulheres = 0

for c in range(1, 5):
    print('---- \033[1;34m{}°\033[m PESSOA ----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    
    media += idade
    
    if y == 0 and sexo == 'M':
        nomeHomem = nome
        velho = idade
        y = 1
    else:
        if sexo == 'M' and idade > velho:
            nomeHomem = nome
            velho = idade
        elif sexo == 'F':
            if idade < 20:
                mulheres += 1
                novinha += 1

media = media / 4
print('\n')
print('A média da idade do grupo é de \033[1;34m{}\033[m '.format(media))
print('O homem mais velho tem \033[1;32m{}\033[m e se chama \033[1;34m{}\033[m'.format(velho, nomeHomem))
print('Ao todo são \033[1;32m{}\033[m mulheres com pelo menos \033[1;33m{}\033[m anos'.format(mulheres, novinha))