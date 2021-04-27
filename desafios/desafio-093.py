#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dicionario = dict()
lista = list()

dicionario['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dicionario["nome"]} jogou?: '))

for c in range(0, partidas):
    lista.append(int(input(f'Quantos gols na partida {c+1}: ')))
dicionario['gols'] = lista[:]
dicionario['total'] = sum(lista)

print('-=' * 30)
print(dicionario)
print('-=' * 30)
for k, v in dicionario.items():
	print(f'{k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dicionario["nome"]} jogou {len(dicionario["gols"])}.')
for c in range(0, len(dicionario["gols"])):
    print(f'Na partida {c+1}, fez {dicionario["gols"][c]}.')
#for i, v in enumerate(jogador['gols']):
#    print(f'    => Na partida {i}, fez {v} gols')
print(f'Foi um total de {dicionario["total"]}.')



'''if c == 1:
    dicionario['total'] = 0
    dicionario['total'] += dicionario['gols']
else: 
    dicionario['total'] += dicionario['gols']'''