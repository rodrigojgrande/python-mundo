#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num=1, show=False):
    """
    -> Calcula o Fatorial de um número
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n;
    """
    f = 1
    for c in range(num, 0, -1):
        if show: 
            print(c, end='')
            if c > 1: 
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


numero = int(input('Indique um valor para fatorizar'))
print(f'O resultado é {fatorial(numero, show=True)}')
help(fatorial)