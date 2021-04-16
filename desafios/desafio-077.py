#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = 'aprender', 'programar', 'estudar', 'linguagem', 'python', 'curso', 'grátis', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        letra.lower() in 'aeiou':
        #Para considerar acentos por exemplo: 'aáàâãeiou':
            print(letra, end=' ')