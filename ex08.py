# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input("Digite um valor em metros para ser convertido em centímetros e milímetros: "))

c = valor * 100
m = valor * 1000

print(f"{valor} metros convertidos em centímetros resultarão em {c} centímetros e {m} milímetros.")