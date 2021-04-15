#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

tupla = ('Astralis', 'Natus', 'Vincere', 'Team Vitality', 'BIG', 'G2 Esports', 'Heroic', 'Team Liquid', 'FURIA Esports', 'Fnatic', 'FaZe Clan', 'FURIA Esports', 'MIBR', 'GODSENT', 'O PLANO')

print(f'Lista de times ESL CSGO: {tupla}')
print('-='*60)
print(f'Os cinco primeiros são: {tupla[0:6]}')
print('-='*60)
print(f'Os quatro últimos são: {tupla[-4:]}')
print('-='*60)
print(f'Os times em ordem alfabética: {sorted(tupla)}')
print('-='*60)
print(f'O MIBR está na {tupla.index("MIBR")+1}° posição')
print('-='*60)
print(f'{len(tupla)}')
