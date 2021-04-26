#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dicionario = dict()
dicionario['nome'] = str(input('Nome: '))
dicionario['media'] = float(input('Média: '))

if dicionario['media'] >= 7:
    dicionario['resultado'] = 'Aprovado'
else:
    dicionario['resultado'] = 'Reprovado'

print(dicionario)

print('-=' * 50)
#print(f'Nome é igual a {dicionario["nome"]}')
#print(f'Média é igual a {dicionario["media"]}')
#print(f'Situação é igual a {dicionario["resultado"]}')

for k, v in dicionario.items():
	print(f'{k} é igual a {v}')