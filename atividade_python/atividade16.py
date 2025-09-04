preco_gasolina = 5.79
preco_etanol = 4.39
preco_diesel = 6.09

combustivel = input("Digite o tipo de combustível (gasolina, etanol ou diesel): ").lower()

if combustivel == "gasolina":
    print(f"O preço da gasolina é R$ {preco_gasolina:.2f} por litro.")
elif combustivel == "etanol":
    print(f"O preço do etanol é R$ {preco_etanol:.2f} por litro.")
elif combustivel == "diesel":
    print(f"O preço do diesel é R$ {preco_diesel:.2f} por litro.")
else:
    print("Tipo de combustível inválido. Tente novamente.")