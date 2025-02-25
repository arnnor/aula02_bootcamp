# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
raio_do_circulo = float(input("Digite o raio do circulo: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
print(f"Essa é a área do circulo de raio = {raio_do_circulo}: {area_do_circulo: .2f}")