#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero  = int(input('Digite um número inteiro:'))

print('Escolha uma das bases para conversão:')
print('[ \033[1;33m1\033[m ] Converter para Binário')
print('[ \033[1;33m2\033[m ] Converter para Octal')
print('[ \033[1;33m3\033[m ] Converter para Hexadecimal')

escolha  = int(input('Sua opção:'))



if escolha == 1:
    resultado = bin(numero)[2:]
    print('\033[1;32m{} convertido para Binário é igual a {}.\033[m'.format(numero, resultado))

elif escolha == 2:
    resultado = oct(numero)[2:]
    print('\033[1;312{} convertido para Octal é igual a {}.\033[m'.format(numero, resultado))

elif escolha == 3: 
    resultado = hex(numero)[2:]
    print('\033[1;32m{} convertido para Hexadecimal é igual a {}.\033[m'.format(numero, resultado))

else: 
    print('\033[1;31mComando inválido!\033[m')
