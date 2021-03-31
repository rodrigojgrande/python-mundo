#Exercício Python 32: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

#Condições
#- Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
#- Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
#- Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.

from datetime import date 

ano = int(input('Me diga um ano qualquer: '))

if (ano == 0):
    ano = date.today().year
if (((ano % 4) == 0) and ((ano % 100) != 0 or (ano % 400) == 0)):
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é Bissexto!'.format(ano))
    
#elif(((ano % 400) == 0)): 
#print('O ano {} é Bissexto!'.format(ano))