print("Escolha a conversão desejada:")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")

opcao = input("Digite 1 ou 2: ")

if opcao == "1":
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F.")

elif opcao == "2":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit:.2f}°F equivalem a {celsius:.2f}°C.")

else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")