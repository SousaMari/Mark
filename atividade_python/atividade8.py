estado_civil = input("Digite seu estado civil (solteiro, casado, divorciado, viúvo): ").lower()

if estado_civil == "solteiro":
    print("Você está solteiro. Aproveite sua liberdade!")
elif estado_civil == "casado":
    print("Você está casado. Que bom compartilhar a vida com alguém!")
elif estado_civil == "divorciado":
    print("Você está divorciado. Recomeços fazem parte da vida.")
elif estado_civil == "viúvo":
    print("Você está viúvo. Que suas memórias tragam conforto.")
else:
    print("Estado civil não reconhecido. Tente novamente.")