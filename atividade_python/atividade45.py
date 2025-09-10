maior_numero = -999999999

print("Por favor, digite 5 números.")
for i in range(5):
    numero = int(input(f"Digite o {i+1}° número: "))
    if numero > maior_numero:
        maior_numero = numero
        print(f"O maior número até agora é: {maior_numero}")    