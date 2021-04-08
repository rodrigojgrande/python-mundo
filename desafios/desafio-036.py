#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Valor da Casa: R$'))
salarioComprador = float(input('Salário do comprador: R$'))
anosFinanciamento = int(input('Quantos anos de financiamento: R$'))


prestacaoMensal = valorCasa / (anosFinanciamento * 12)

limite = salarioComprador * 0.3

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valorCasa, anosFinanciamento, prestacaoMensal))


if prestacaoMensal > limite:
    print('\033[1;31mEmpréstimo negado!\033[m')
else: 
    print('\033[1;32mEmpréstimo pode ser concedido!\033[m')