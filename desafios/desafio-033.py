#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#MY STYLE

if ((a > b and a < c)):
    print('O menor valor digitado foi {}'.format(b))
    print('O maior valor digitado foi {}'.format(c))
elif ((b > a and b < c)): 
    print('O menor valor digitado foi {}'.format(a))
    print('O maior valor digitado foi {}'.format(c))
elif ((c > a and c < b)): 
    print('O menor valor digitado foi {}'.format(a))
    print('O maior valor digitado foi {}'.format(b))
elif ((a > c and a < b)): 
    print('O menor valor digitado foi {}'.format(c))
    print('O maior valor digitado foi {}'.format(b))
elif ((b > c and b < a)): 
    print('O menor valor digitado foi {}'.format(c))
    print('O maior valor digitado foi {}'.format(a))
elif ((c > b and c < a)): 
    print('O menor valor digitado foi {}'.format(b))
    print('O maior valor digitado foi {}'.format(a))
    
    

#TEACHER STYLE
#Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
    
#Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
    
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))