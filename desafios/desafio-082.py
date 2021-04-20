#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
par = []
impar = []

while True:
    value = int(input(f'Digite um valor: '))
    lista.append(int(value))
    if value % 2 == 0:
        par.append(int(value))
    else:
        impar.append(int(value))
    again = str(input('\033[1;33mQuer continuar [S/N]:\033[m ').strip().upper()[0])
    if again == 'N':
        break

print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista impares é: {impar}')
