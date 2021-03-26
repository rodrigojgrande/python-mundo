#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float (input('Qual a largura da parede em metros?'))
altura = float (input('E a altura da parede em metros?'))
tinta = 2
area = largura*altura
quantidade = area / tinta
print('Sua parede têm a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede, você precisará de {}l.'. format(largura, altura, area, quantidade))