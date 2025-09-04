nota = float(input("Digite uma nota entre 0 e 10: "))

if nota < 0 or nota > 10:
    print("Nota inválida. Digite um valor entre 0 e 10.")
elif nota < 4:
    print("Classificação: Baixa")
elif nota <= 7:
    print("Classificação: Média")
else:
    print("Classificação: Alta")