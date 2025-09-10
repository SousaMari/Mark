numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}° número: "))
    numeros.append(numero)

print("\nOs Números pares que você digitou são:")

for numero in numeros:
    if numero % 2 == 0:
        print(numero)
