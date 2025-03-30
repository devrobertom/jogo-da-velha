import os

# Função para inicializar o tabuleiro
def inicializar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

# Função para verificar se alguém venceu
def verificar_vitoria(tabuleiro, jogador):
    # Verificando linhas, colunas e diagonais
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or \
           all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

# Função para verificar empate
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if ' ' in linha:
            return False
    return True

# Função para salvar o resultado do jogo em um arquivo
def salvar_resultado(nome_jogador1, nome_jogador2, placar, tabuleiro):
    if not os.path.exists('resultados'):
        os.makedirs('resultados')
    
    nome_arquivo = f'resultados/{nome_jogador1}_vs_{nome_jogador2}.txt'
    with open(nome_arquivo, 'w') as f:
        f.write(f'Jogo: {nome_jogador1} vs {nome_jogador2}\n')
        f.write(f'Placar: {placar[0]} x {placar[1]}\n')
        f.write('Tabuleiro final:\n')
        for linha in tabuleiro:
            f.write('|'.join(linha) + '\n')
            f.write('-' * 5 + '\n')

# Função para jogar uma rodada
def jogar_rodada(jogador, tabuleiro):
    while True:
        try:
            jogada = int(input(f'Jogador {jogador}, escolha a posição (1-9): ')) - 1
            linha = jogada // 3
            coluna = jogada % 3
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogador
                break
            else:
                print('Posição já ocupada, tente novamente!')
        except (ValueError, IndexError):
            print('Entrada inválida, escolha um número entre 1 e 9.')

# Função principal
def main():
    print("Bem-vindo ao Jogo da Velha!")
    nome_jogador1 = input("Digite o nome do jogador 1: ")
    nome_jogador2 = input("Digite o nome do jogador 2: ")

    tabuleiro = inicializar_tabuleiro()
    jogadores = [nome_jogador1, nome_jogador2]
    simbolos = ['X', 'O']
    placar = [0, 0]
    turno = 0

    while True:
        exibir_tabuleiro(tabuleiro)
        jogar_rodada(simbolos[turno], tabuleiro)
        
        if verificar_vitoria(tabuleiro, simbolos[turno]):
            exibir_tabuleiro(tabuleiro)
            print(f'Jogador {jogadores[turno]} venceu!')
            placar[turno] += 1
            break
        elif verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print('Empate!')
            break

        turno = 1 - turno  # Alterna entre os jogadores

    salvar_resultado(nome_jogador1, nome_jogador2, placar, tabuleiro)

if __name__ == '__main__':
    main()
