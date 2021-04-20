#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
again = 'S'

while True:
    value = int(input(f'Digite um valor: '))
    
    if value in lista:
        print('Valor duplicado! Não vou adicionar...')

    else:
        lista.append(int(value))
        print('Valor adicionado com sucesso...')

    print(lista)
    
    again = str(input('\033[1;33mQuer continuar [S/N]:\033[m ').strip().upper()[0])
    if again == 'N':
        break
    
print(sorted(lista))