#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

preco = 0
carinhos = 0
baratinho = 0
total = 0
c = 0

while True:
    print('-'*30)
    print('---- \033[1;34mLOJA SUPER BARATÃO\033[m ----')
    print('-'*30)
    
    produto = str(input('Nome do Produto: ').strip().upper())
    preco = float(input('Preço: R$'))
    
    if c == 0:
        baratinho = preco
        c += 1
    
    if preco < baratinho:
        baratinho = preco 
    
    if preco > 1000:
        carinhos += 1
        
    total += preco
        
    again = str(input('\033[1;33mQuer continuar [S/N]:\033[m ').strip().upper()[0])
    
    if again == 'N':
        break
    
print('O total da compra foi: \033[1;32mR${:.2f}\033[m '.format(total))
print('Temos \033[1;32m{:.2f}\033[m produtos custando mais de R$1000'.format(carinhos))
print('O produto mais barato foi Lapiseira que custa \033[1;32mR${:.2f}\033[m'.format(baratinho))
