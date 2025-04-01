import os

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
