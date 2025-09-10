numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}° número: "))
    numeros.append(numero)  

soma = sum(numeros)

print("\nNúmeros digitados:", numeros)
print("Soma dos números:", soma)    