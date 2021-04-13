#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

#MINHA SOLUÇÃO
#r = ''
#while r !='M' and r !='F':
#   r = str(input('Informe seu sexo [M/F]: ').upper().strip()[0])
#   if r !='M' or r !='F':
#       r = str(input('Dado inválido. Por favor, informe seu sexo [M/F]: ').upper())

#TEACHER
sexo = str(input('Informe seu sexo [M/F]: ').upper().strip()[0])
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido. Por favor, informe seu sexo [M/F]: ').upper().strip()[0])
print('Sexo {} registrado com sucesso'.format(sexo))