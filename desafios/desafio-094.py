#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

dicionario = dict()
lista = list()
idadeTotal = 0
soma = media = 0
while True:
    dicionario['nome'] = str(input('Nome: '))
    dicionario['sexo'] = str(input('Sexo [M/F]: ').upper().strip()[0])
    while dicionario['sexo'] not in 'MF':
        dicionario['sexo'] = str(input('Dado inválido. Por favor, informe seu sexo [M/F]: ').upper().strip()[0])
    dicionario['idade'] = int(input('Idade: '))
    lista.append(dicionario.copy())
    soma += dicionario['idade']
    resposta = str(input('Quer continuar? [S/N] ').upper().strip()[0])
    
    while resposta not in 'SN':
        resposta = str(input('Dado inválido. Por favor, responda com [S/N] ').upper().strip()[0])

    if resposta == 'N':
        break
    elif resposta == 'S':
        continue

#ALGUMAS TENTATIVAS FRUSTRADAS
'''for dicionario in lista:
    for v in dicionario.values():
        print(v, end='')
    print()'''   
    
'''for dicionario in lista:
    for k, v in dicionario.items():
        for k in 'idade':
            idadeTotal += v
        print(f'O campo {k} tem valor {v}')'''
        
'''for c in range(0, len(lista)):
    print(lista['dicionario']['idade'])'''
    
media = soma / len(lista)

print(f'A) Ao todo temos {len(lista)} pessoas cadastradas')
print(f'B) A média da idade é de {media:5.2f} anos')
print(f'C) As mulheres casdastradas foram ', end='')
for dicionario in lista:
    if dicionario['sexo'] in 'Ff':
        print(f'{dicionario["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média ')
for dicionario in lista:
    if dicionario['idade'] >= media:
        print('     ', end='')
        for k, v in dicionario.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRANDO >>')
#print(lista)
