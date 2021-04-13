#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('='*30)
print(' '*5, '\033[1;33m10 TERMOS DE UMA PA\033[m', ' '*5, )
print('='*30)

primeiro = int (input('Primeiro Termo: '))
razao =  int (input('Razão: '))

x = 0

while x != 10:
    print('{} '.format(primeiro), end='-> ')
    primeiro += razao
    x += 1
print('It s Over!')

