transporte = input("Escolha um modo de transporte (carro, bicicleta, a pé): ")

if transporte == "carro":
    print("A velocidade média do carro é de 100 km/h.")
elif transporte == "bicicleta":
    print("A velocidade média da bicicleta é de 20 km/h.")
elif transporte == "a pé":
    print("A velocidade média a pé é de 5 km/h.")
else:
    print("Modo de transporte inválido.")