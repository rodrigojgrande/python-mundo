#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno de {largura:.1f}x{comprimento:.1f} é de {area:.1f}m²')


print('Controle de Terrenos')
print('-'* 30)
largura = float(input('LARGURA (m):'))
comprimento = float(input('COMPRIMENTO (m):'))

area(largura, comprimento)