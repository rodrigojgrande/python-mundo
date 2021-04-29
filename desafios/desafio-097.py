#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: escreva(‘Olá, Mundo!’) Saída:
#~~~~~~~~~ 
#Olá, Mundo!    
#~~~~~~~~~          

def escreve(frase):
    tamanho = (len(frase) + 4)
    print('~' * tamanho)
    print(f'{frase:^{tamanho}}')
    print('~' * tamanho)
    

mensagem = str(input('Digite uma mensagem: '))
escreve(mensagem)