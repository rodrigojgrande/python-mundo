#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))

#MINHA CONCLUSÃO
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Os segmentos acima podem formar um triângulo \033[1;32mEQUILÁTERO\033[m')
    elif a == b or a == c or b == c:
        print('Os segmentos acima podem formar um triângulo \033[1;33mISÓSCELES\033[m')
    elif a != b and a != c and b != c:
        print('Os segmentos acima podem formar um triângulo \033[1;34mESCALENO\033[m')
    else:
        print('\033[1;31opsss! Algo de inesperado aconteceu!\033[m')
else:
    print('\033[1;31mOs segmentos acima não podem formar um triângulo\033[m')

#PROFESSOR
#if a == b == c:
#    print('Os segmentos acima podem formar um triângulo \033[1;32mEQUILÁTERO\033[m')
#elif a != b != c != a:
#    print('Os segmentos acima podem formar um triângulo \033[1;34mESCALENO\033[m')
#else:
#    print('Os segmentos acima podem formar um triângulo \033[1;33mISÓSCELES\033[m')