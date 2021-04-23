#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


#MY WAY
'''princ = list()
temp = list()
for c in range(1, 8):
    temp.append(int(input(f'Digite o {c}° valor: ')))
    if temp[0] % 2 == 0:
        temp.append(str('par'))
    else:
        temp.append(str('impar'))
    princ.append(temp[:])
    temp.clear()
print('Os valores pares digitados foram:', end='')
for p in princ:
    if p[1] == 'par':
        print(f'[{p[0]}] ', end='')
print()
print('Os valores impares digitados foram:', end='')
for i in princ:
    if i[1] == 'impar':
        print(f'[{i[0]}] ', end='')'''
        
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else: 
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')