#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
again = 'S'
cont = 0

while True:
    lista.append(int(input(f'Digite um valor: ')))
    
    cont += 1
    
    again = str(input('\033[1;33mQuer continuar [S/N]:\033[m ').strip().upper()[0])
    if again == 'N':
        break

print(f'Foram digitados {cont} digitos')
print(sorted(lista, reverse=True))
    
if 5 in lista:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')