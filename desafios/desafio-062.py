#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('='*30)
print(' '*5, '\033[1;33m10 TERMOS DE UMA PA\033[m', ' '*5, )
print('='*30)

primeiro = int (input('Primeiro Termo: '))
razao =  int (input('Razão: '))

x = 0
y = 10

fim = False

while fim != True:
    while x < y:
        print('{} '.format(primeiro), end='-> ')
        primeiro += razao
        x += 1
    print('Pausa!')
    add = int (input('Quantos termos você quer adicionar? '))
    y += add
    if x == y:
        fim = True
print('Progressão finalizadas com {} termos mostrados!'.format(y))

