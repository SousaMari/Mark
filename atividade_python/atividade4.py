cor = input("Digite uma cor vermelho,verde ou azul):")
cor = cor.strip().lower()

if cor == "vermelho":
    print("Você escolheu vermelho! Uma cor cheia de energia e paixão.")
elif cor == "verde":
    print("Você escolheu verde! A cor da natureza e da tranquilidade.")
elif cor == "azul":
    print("Você escolheu azul! Representa calma, confiança e serenidade.")
else:
    print("Cor inválida. Por favor, escolha entre vermelho, verde ou azul.")


