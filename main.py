from modules.tabuleiro import inicializar_tabuleiro, exibir_tabuleiro
from modules.verificacoes import verificar_vitoria, verificar_empate
from modules.jogador import jogar_rodada
from modules.salvar import salvar_resultado

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
