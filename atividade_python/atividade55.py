numero = int(input("Digite um número maior que 100: "))
while numero <= 100:
    print("Número inválido.Ele deve ser maior que 100.")
    numero = int(input("Tente novamente: "))
print(f"Número aceito: {numero}")    