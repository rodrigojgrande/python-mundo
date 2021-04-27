#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date 
ano = date.today().year

dicionario = dict()
dicionario['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dicionario['idade'] = ano - nascimento
dicionario['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dicionario['ctps'] != 0:
    dicionario['contratacao'] = int(input('Ano de contratação: '))
    dicionario['salario'] = int(input('Salário R$: '))
    dicionario['aposentadoria'] = dicionario['idade'] + ((dicionario['contratacao']+35) - ano)

for k, v in dicionario.items():
	print(f'{k} tem o valor {v}')

