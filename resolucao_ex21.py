# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
# garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
    celcius = float(input("Digite a temperatura em Celcius: "))

    fahrenheit = (celcius * 5/9) + 32

    print(f"{celcius}C° é igual a {fahrenheit}°F")
except ValueError:
    print("Por favor, digite um número válido para a temperatura.")