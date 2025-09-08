valor_produto = float(input("Digite o valor do produto: "))
desconto = valor_produto * 0.10

valor_final = valor_produto - desconto

print(f"O valor do desconto é: R$ {desconto:.2f}")
print(f" O valor final do produto com deconto é: R$ {valor_final:.2f}")
