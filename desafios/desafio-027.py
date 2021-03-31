#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()

lista = nome.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu último nome é {}'.format(lista[-1]))

#Método Professor:
#print('Seu último nome é {}'.format(lista[len(lista)-1]))