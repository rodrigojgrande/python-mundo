#01. Considere uma tupla chamada países que tem vários elementos. Como fazemos para mostrar o primeiro e o último elemento dessa tupla?
print('01. Considere uma tupla chamada países que tem vários elementos. Como fazemos para mostrar o primeiro e o último elemento dessa tupla?')
print('\033[1;32mR: print(países[0], países[-1])\033[m')

print('\n')

#02. Considerando a declaração pessoas = [['Pedro', 25], ['Maria', 12], ['José', 25]] feita em Python, que valor aparecerá na tela se executarmos o comando print(pessoas[2][1])?
print('02. Considerando a declaração pessoas = [["Pedro", 25], ["Maria", 12], ["José", 25]] feita em Python, que valor aparecerá na tela se executarmos o comando print(pessoas[2][1])?')

pessoas = [['Pedro', 25], ['Maria', 12], ['José', 25]]
print(pessoas[2][1])

print('\033[1;32mR: 25\033[m')

print('\n')

#03. Qual das estruturas compostas do Python é tida como "imutável"?
print('03. Qual das estruturas compostas do Python é tida como "imutável"?')
print('\033[1;32mR: tupla\033[m')

print('\n')

#04. Qual é a principal diferença dos dicionários em Python em relação às tuplas e listas.
print('04. Qual é a principal diferença dos dicionários em Python em relação às tuplas e listas.')
print('\033[1;32mR: em dicionários, os índices podem ser nomeados\033[m')

print('\n')

#05. Considere uma tupla pontos, com 20 elementos numéricos. Como podemos mostrar todos os valores armazenados em ordem crescente?
print('05. Considere uma tupla pontos, com 20 elementos numéricos. Como podemos mostrar todos os valores armazenados em ordem crescente?')
print('\033[1;32mR: print(sorted(pontos))\033[m')

print('\n')

#06. Em que local vamos escrever o texto que vai servir como DOCSTRINGS de uma determinada função?
print('06. Em que local vamos escrever o texto que vai servir como DOCSTRINGS de uma determinada função?')
print('\033[1;32mR: depois da linha de declaração da função, abaixo da linha def\033[m')

print('\n')

#07. Quando declaramos uma lista Python com num = [3, 6, 4, 1] e executamos a estrutura for n1, n2 in enumerate(num): com o comando print(n1 + n2) dentro do bloco do laço, quais valores serão exibidos?
print('07. Quando declaramos uma lista Python com num = [3, 6, 4, 1] e executamos a estrutura for n1, n2 in enumerate(num): com o comando print(n1 + n2) dentro do bloco do laço, quais valores serão exibidos?')

num = [3, 6, 4, 1]
for n1, n2 in enumerate(num):
    print(n1 + n2) 
    
print('\033[1;32mR: 3, 7, 6, 4\033[m')

print('\n')

#08. Quando queremos criar uma função chamada somador em Python, qual linha usamos na declaração?
print('08. Quando queremos criar uma função chamada somador em Python, qual linha usamos na declaração?')
print('\033[1;32mR:def somador():\033[m')

print('\n')

#09. Considere a lista num = [2, 8, 4, 7]. Logo em seguida, vamos executar - nessa ordem - os comandos num.pop(), depois num.insert(1, 3) e por fim num.append(6). Se executarmos o comando print(num), o que será exibido na tela?
print('09. Considere a lista num = [2, 8, 4, 7]. Logo em seguida, vamos executar - nessa ordem - os comandos num.pop(), depois num.insert(1, 3) e por fim num.append(6). Se executarmos o comando print(num), o que será exibido na tela?')

num = [2, 8, 4, 7]
num.pop()
num.insert(1, 3)
num.append(6)
print(num)

print('\033[1;32mR: [2, 3, 8, 4, 6]\033[m')

print('\n')

#10. Na linha de declaração def teste(a, b=1, c=2):, quantos parâmetros são obrigatórios?
print('10. Na linha de declaração def teste(a, b=1, c=2):, quantos parâmetros são obrigatórios?')
print('\033[1;32mR:um:\033[m')
