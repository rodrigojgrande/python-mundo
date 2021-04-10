#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
#A Progressão Aritmética (P.A.) é uma sequência de números onde a diferença entre dois termos consecutivos é sempre a mesma. 
print('='*30)
print(' '*5, '\033[1;33m10 TERMOS DE UMA PA\033[m', ' '*5, )
print('='*30)

primeiro = int (input('Primeiro Termo: '))
razao =  int (input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('Acabou!')
