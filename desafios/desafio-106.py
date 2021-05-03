#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

from time import sleep

cor = ('\033[m',        # 0 - sem cores 
    '\033[0;30;41m',    # 1 - vermelho
    '\033[0;30;42m',    # 2 - verde
    '\033[0;30;43m',    # 3 - amarelo
    '\033[0;30;44m',    # 4 - azul
    '\033[0;30;45m',    # 5 - roxo
    '\033[7;30m'        # 6 - branco
    );
    
def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 4)
    print(cor[6], end='')
    help(comando)
    print(cor[0], end='')
    sleep(2)
    
def titulo(msg, c=0):
    tamanho = len(msg) + 4
    print(cor[c], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(cor[0], end='')
    sleep(1)
    
#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else: 
        ajuda(comando)
titulo('ATÉ LOGO', 1)
            