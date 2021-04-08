#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) /2

print('Tirando \033[1;34m{:.1f}\033[m e \033[1;34m{:.1f}\033[m, a média é \033[1;35m{:.1f}\033[m'.format(n1, n2, media))

if media < 5:
    print('O aluno está \033[1;31mReprovado\033[m')
elif media >= 5 and media < 6.9:
    print('O aluno está \033[1;33mRecuperação\033[m')
elif media >= 7:
    print('O aluno está \033[1;32mAprovado\033[m')
else:
    print('\033[1;32mComando inválido!\033[m')

