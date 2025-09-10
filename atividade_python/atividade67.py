def exibir_tabuleiro(tabuleiro):
    print("\n")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True
    
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True
    
    if all(tabuleiro[i][i] == jogador for i in range(3)) or \
       all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def verificar_empate(tabuleiro):
    return all(celula in ["X", "O"] for linha in tabuleiro for celula in linha)

def jogo_da_velha():
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


jogo_da_velha()