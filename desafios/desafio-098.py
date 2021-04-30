#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:   
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1 #Expressão que converse um número negativo para positivo (- * - = +)
    if p == 0:
        p = 1
    print('-=' * 40)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else: 
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início:'))
fim = int(input('fim:'))
pas = int(input('Passo:'))
contador(ini, fim, pas)

#MINHA LÓGICA
'''def conta(inicio, fim, passo):
    for c in range(inicio, fim+passo, passo):
        print(c, end=' ')

for c in range(1, 11, 1):
	print(c, end=' ')

print('-=' * 40)

for c in range(10, 0, -1):
	print(c, end=' ')

print('-=' * 40)

#for c in range(12, -10, -7):
#	print(c, end=' ')''

print('Agora é a sua vez de personalizar essa contagem!')
inicio = int(input('Início:'))
fim = int(input('fim:'))
passo = int(input('Passo:'))
conta(inicio, fim, passo)'''