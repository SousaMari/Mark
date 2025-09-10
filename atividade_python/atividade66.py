# Lista para armazenar os nomes
nomes = []

while True:
    print("\nMenu de Operações:")
    print("1 - Cadastrar nome")
    print("2 - Atualizar nome")
    print("3 - Excluir nome")
    print("4 - Listar todos os cadastrados")
    print("Digite qualquer outra coisa para encerrar.")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_nome = input("Digite o nome a ser cadastrado: ")
        nomes.append(novo_nome)
        print(f"✅ Nome '{novo_nome}' cadastrado com sucesso.")

    elif opcao == "2":
        nome_antigo = input("Digite o nome que deseja atualizar: ")
        if nome_antigo in nomes:
            novo_nome = input("Digite o novo nome: ")
            index = nomes.index(nome_antigo)
            nomes[index] = novo_nome
            print(f"✅ Nome '{nome_antigo}' atualizado para '{novo_nome}'.")
        else:
            print(f"⚠️ Nome '{nome_antigo}' não encontrado.")

    elif opcao == "3":
        nome_excluir = input("Digite o nome que deseja excluir: ")
        if nome_excluir in nomes:
            nomes.remove(nome_excluir)
            print(f"✅ Nome '{nome_excluir}' excluído com sucesso.")
        else:
            print(f"⚠️ Nome '{nome_excluir}' não encontrado.")

    elif opcao == "4":
        if nomes:
            print("📋 Lista de nomes cadastrados:")
            for nome in nomes:
                print("-", nome)
        else:
            print("📭 Nenhum nome cadastrado.")

    else:
        print("Encerrando o programa. Até mais!")
        break

    # Pergunta se o usuário deseja continuar
    continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
    if continuar != "s":
        print("Encerrando o programa. Obrigado por usar!")
        break