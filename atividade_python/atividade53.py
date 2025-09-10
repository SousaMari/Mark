numero = int(input("Digite um número para iniciar a contagem regressiva: "))
print(f"\nContagem regressiva de {numero} até 1:")

for i in range(numero, 0, -1):
    print(i)