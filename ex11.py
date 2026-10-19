# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros.

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura
tinta = area / 2

print(f"A largura da parede é de {largura} metros.")
print(f"A altura da parede é de {altura} metros.")
print(f"Será necessário {tinta:.2f} litros de tinta para pintar a parede.")