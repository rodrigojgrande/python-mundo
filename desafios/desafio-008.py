#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

#km == Quilômetro
#dam == Decâmetro 
#m == Metro
#dm == Decímetro  
#cm == Centímetro 
#mm == Milímetro

x = float (input('Digite o valor em metros: '))
km = x /1000
hm = x/100
dam = x/10
m = x
dm = x*10
cm = x*100
mm = x*1000

print('Uma distância em {} metros equivale a: \n{} km \n{} hm \n{} dam \n{} m \n{} dm \n{} cm \n{} mm'. format(x, km, hm, dam, m, dm, cm, mm))