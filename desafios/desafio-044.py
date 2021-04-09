#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

print('='*15, '\033[1;33mLOJAS GUANABARA\033[m', '='*15, )

preco = float(input('Preço das compras: R$'))

print('\033[1;33mFORMAS DE PAGAMENTO\033[m')
print('[ \033[1;33m1\033[m ] à vista dinheiro/cheque')
print('[ \033[1;33m2\033[m ] à vista cartão')
print('[ \033[1;33m3\033[m ] 2x no cartão')
print('[ \033[1;33m4\033[m ] 3x ou mais no cartão')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco * 0.90
    print('Sua compra \033[1;34mà vista dinheiro/cheque\033[m de \033[1;32mR${:.2f}\033[m vai custar \033[1;32mR${:.2f}\033[m no final'.format(preco, total))
elif opcao == 2:
    total = preco * 0.95
    print('Sua compra \033[1;34mà vista no cartão\033[m de \033[1;32mR${:.2f}\033[m vai custar \033[1;32mR${:.2f}\033[m no final'.format(preco, total))
elif opcao == 3:
    total = preco * 0.95
    print('Sua compra \033[1;34mde 2x no cartão\033[m de \033[1;32mR${:.2f}\033[m vai custar \033[1;32mR${:.2f}\033[m cada parcela'.format(preco, preco / 2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = preco * 1.20
    print('Sua compra \033[1;34mde {}x no cartão\033[m de \033[1;32mR${:.2f}\033[m vai custar \033[1;32mR${:.2f}\033[m no total, sendo cada parcela no valor de \033[1;32mR${:.2f}\033[m'.format(parcelas, preco, total, total / parcelas))
else:
    print('\033[1;31opsss! Algo de inesperado aconteceu!\033[m')
