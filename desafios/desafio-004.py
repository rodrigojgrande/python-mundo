#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(n))
print('Só têm espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É decimal?', n.isdecimal())
print('É alfanumérico?', n.isalnum())
print('É um digito?', n.isdigit())
print('É um ID?', n.isidentifier())
print('É visualizavél?', n.isprintable())
print('É capitalizado?', n.istitle())
print('É maísculas?', n.isupper())
print('É minúsculas?', n.islower())

