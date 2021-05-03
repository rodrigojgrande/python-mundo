#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas 
#– A maior nota
#– A menor
#– A média da turma 
#– A situação (opcional)

def notas(*valor, show=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param valor: Uma ou mais notas dos alunos (aceita várias)
    :param show: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre e situações da turma.
    """
    
    dicionario = dict()
    dicionario['total'] = len(valor)
    dicionario['maior'] = max(valor)
    dicionario['menor'] = min(valor)
    dicionario['media'] = sum(valor)/len(valor)
    if show: 
        if dicionario['media'] >= 7:
            dicionario['situacao'] = 'BOA'
        elif dicionario['media'] >= 5:
            dicionario['situacao'] = 'RAZOAVEL'
        else:
            dicionario['situacao'] = 'RUIM'
            
    return dicionario    


resposta = notas(5.5,2.5,1.5,show=True )
print(resposta)
help(notas)