contador = 0

for i in range(7):
    numero = float(input(f"Digite o {i+1}° número: "))
    if numero > 10:
        contador += 14
print(f"\nVocê digitou {contador} número(s) maior(es) que 10.")        


