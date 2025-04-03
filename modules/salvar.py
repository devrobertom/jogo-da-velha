import os

def salvar_resultado(nome_jogador1, nome_jogador2, placar, historico_partidas):
    if not os.path.exists('resultados'):
        os.makedirs('resultados')

    nome_arquivo = f'resultados/{nome_jogador1}_vs_{nome_jogador2}.txt'
    with open(nome_arquivo, 'w') as f:
        f.write(f'Jogo: {nome_jogador1} vs {nome_jogador2}\n')
        f.write(f'Placar Final: {placar[0]} x {placar[1]}\n\n')

        for i, (tabuleiro, historico) in enumerate(historico_partidas, start=1):
            f.write(f'--- Partida {i} ---\n')
            f.write("Histórico de jogadas:\n")
            for rodada, (jogador, posicao) in enumerate(historico, start=1):
                f.write(f'Rodada {rodada}: {jogador} jogou na posição {posicao + 1}\n')

            f.write("\nTabuleiro final:\n")
            for linha in tabuleiro:
                f.write(' | '.join(linha) + '\n')
                f.write('-' * 9 + '\n')

            f.write("\n")

    print(f"Histórico da partida foi salvo em {nome_arquivo}")

