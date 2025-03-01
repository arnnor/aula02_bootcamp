try:
    celcius = float(input("Digite a temperatura em Celcius: "))

    fahrenheit = (celcius * 5/9) + 32

    print(f"{celcius}C° é igual a {fahrenheit}°F")
except ValueError:
    print("Por favor, digite um número válido para a temperatura.")