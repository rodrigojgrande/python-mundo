#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois

a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))

#MELHOR RESPOSTA
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem formar um triângulo')


#MINHA LINHA DE PENSAMENTO
#Verificando quem é o menor
#menor = a
#if b < a and b < c:
#    menor = b
#if c < a and c < b:
#    menor = c
#    
#Verificando quem é o maior
#maior = a
#if b > a and b > c:
#    maior = b
#if c > a and c > b:
#    maior = c
#    
#Verificando quem é o meio
#meio = a
#if a > b and b > c:
#    meio = b
#if c > b and b > a:
#    meio = b
#if a > c and c > b:
#    meio = c
#if b > c and c > a:
#    meio = c
#    
#print('O menor valor digitado foi {}'.format(maior))
#print('O menor valor digitado foi {}'.format(menor))
#print('O meio valor digitado foi {}'.format(meio))
#
#if ((menor + meio) > maior):
#    print('Os segmentos acima podem formar um triângulo')
#else:
#    print('Os segmentos acima não podem formar um triângulo')


