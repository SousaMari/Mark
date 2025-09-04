mes = int(input("Digite o número do mês (1 a 12): "))

if mes == 12 or mes == 1 or mes == 2:
    print("A estação do ano é Verão.")
elif mes == 3 or mes == 4 or mes == 5:
    print("A estação do ano é Outono.")
elif mes == 6 or mes == 7 or mes == 8:
    print("A estação do ano é Inverno.")
elif mes == 9 or mes == 10 or mes == 11:
    print("A estação do ano é Primavera.")
else:
    print("Mês inválido. Digite um número entre 1 e 12.")