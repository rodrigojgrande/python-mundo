#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.



def voto(nascimento):
    from datetime import date 
    ano = date.today().year
    idade = ano - nascimento
    
    if idade < 18 and idade >= 16 or idade > 65:
        return 'OPCIONAL' 
    elif idade >= 18:
        return 'VOTA'
    else:
        return 'NÃO VOTA'

nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))

