#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = (input('Em que cidade você nasceu? ')).strip()
cidade = cidade.upper()
primeiro = cidade.split()

print('SANTO' in primeiro[0])