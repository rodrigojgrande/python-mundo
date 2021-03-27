#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float (input('Informe a temperatura em C°: '))
fahrenheit = (celsius * 1.8) + 32


print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!.'. format(celsius, fahrenheit))