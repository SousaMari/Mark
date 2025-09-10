def exibir_tabuleiro(tabuleiro):
    print("\n")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
   
    combinacoes = [
       
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Colunas
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonais
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    return any(all(tabuleiro[l][c] == jogador for l, c in combinacao) for combinacao in combinacoes)

def verificar_empate(tabuleiro):
    return all(celula in ["X", "O"] for linha in tabuleiro for celula in linha)

def jogar_partida():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    print(" Bem-vindo ao Jogo da Velha!")
    exibir_tabuleiro(tabuleiro)

    while True:
        try:
            linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1 ou 2): "))
            coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1 ou 2): "))
        except ValueError:
            print(" Entrada inválida. Digite números entre 0 e 2.")
            continue

        if linha not in range(3) or coluna not in range(3):
            print(" Posição fora do tabuleiro. Tente novamente.")
            continue

        if tabuleiro[linha][coluna] != " ":
            print(" Essa posição já está ocupada. Escolha outra.")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        exibir_tabuleiro(tabuleiro)

        if verificar_vitoria(tabuleiro, jogador_atual):
            print(f" Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            print(" Empate! Ninguém venceu.")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

def jogo_da_velha():
    while True:
        jogar_partida()
        resposta = input("\nDeseja jogar novamente? (s/n): ").lower()
        if resposta != "s":
            print("👋 Obrigado por jogar! Até a próxima.")
            break


jogo_da_velha()