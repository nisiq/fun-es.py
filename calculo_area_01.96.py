#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largula e comprimento) e calcule a área
import time

print("\033[1m=========== Calculador de área ===========")
print("")

l = (float(input("Digite a largura do terreno: ")))
c = (float(input("Digite o comprimento do terreno: ")))
print("")
print(">>>>>>>>>>> Calculando a área <<<<<<<<<<<<")
time.sleep(4)

area = l*c

print(f"De acordo com as dimensões, a área do terreno é de {area}m²")
