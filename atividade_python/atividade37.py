numero = int(input("Digite um número: "))


if numero % 2 == 0 or numero % 5 == 0:
    print(f"O número {numero} é múltiplo de 2 ou de 5.")
else:
    print(f"O número {numero} não é múltiplo de 2 nem de 5.")