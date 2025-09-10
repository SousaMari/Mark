while True:
    primeiro = float(input("Digite o primeiro número: "))
    segundo = float(input("Digite o segundo número: ")) 

    if primeiro > segundo:
        print("O primeiro número é maior que o segundo. ")
        break
    else:
        print("O primeiro número não é maior que o segundo. Tente novamente.")  