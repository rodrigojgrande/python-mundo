#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

#MY WAY
#valores = list()
#for cont in range(0, 5):
#    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

#menor = maior = 0
#init = True

#for c, v in enumerate(valores):
#    if init == True:
#        maior = menor = v
#        init = False
#        print(f'Na posição {c} encontrei o valor {v}!')
#    else: 
#        if v > maior:
#            maior = v
#        if v < menor:
#            menor = v 
#    print(f'Na posição {c} encontrei o valor {v}!')
#print(f'O maior valor foi {maior} na posição {valores.index(maior)}')
#print(f'O menor valor foi {menor} na posição {valores.index(menor)}')
#print('Cheguei ao final da lista.')

#TEACHER WAY
listanum = [];
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
