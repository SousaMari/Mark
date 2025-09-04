numero = input("Digite um número: ")
try:
    numero = int(numero)

    if numero > 10:
        print("O número é maior que 10.")
    else:
        print("O número não é maior que 10.")  
except ValueError:
    print("Você não digitou um número válido!")     