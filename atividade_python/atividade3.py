dias = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]
numero = int(input("Digite um número de 1 a 7: ")) 
if 1 <= numero <= 7:
    print(dias[numero - 1])
else:
    print("Número inválido!")    

                         