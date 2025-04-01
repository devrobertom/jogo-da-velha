def inicializar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)
