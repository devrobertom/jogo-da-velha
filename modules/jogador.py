def jogar_rodada(jogador, tabuleiro):
    while True:
        try:
            jogada = int(input(f'Jogador {jogador}, escolha a posição (1-9): ')) - 1
            linha = jogada // 3
            coluna = jogada % 3
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogador
                return jogada 
            else:
                print('Essa posição já está ocupada, tente novamente!')
        except (ValueError, IndexError):
            print('Valor inválido, deve ser escolhido um número entre 1 e 9.')