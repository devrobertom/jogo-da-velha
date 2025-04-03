from modules.tabuleiro import inicializar_tabuleiro, exibir_tabuleiro
from modules.verificacoes import verificar_vitoria, verificar_empate
from modules.jogador import jogar_rodada
from modules.salvar import salvar_resultado

def main():
    print("Bem-vindo ao Jogo da Velha!")
    nome_jogador1 = input("Digite o nome do jogador 1: ").strip()
    nome_jogador2 = input("Digite o nome do jogador 2: ").strip()

    jogadores = [nome_jogador1, nome_jogador2]
    simbolos = ['X', 'O']
    placar = [0, 0] 
    historico_partidas = [] 

    while True:
        print("\n--- Placar Atual ---")
        print(f"{jogadores[0]}: {placar[0]} | {jogadores[1]}: {placar[1]}")
        print("---------------------\n")

        comando = input('Digite "sair" para encerrar ou pressione Enter para continuar: ').strip().lower()
        if comando == 'sair':
            break

        tabuleiro = inicializar_tabuleiro()
        turno = 0
        historico_jogo = []  

        while True:
            exibir_tabuleiro(tabuleiro)
            posicao = jogar_rodada(simbolos[turno], tabuleiro)
            historico_jogo.append((jogadores[turno], posicao))

            if verificar_vitoria(tabuleiro, simbolos[turno]):
                exibir_tabuleiro(tabuleiro)
                print(f'Jogador {jogadores[turno]} venceu esta rodada!')
                placar[turno] += 1
                break
            elif verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print('Empate!')
                break

            turno = 1 - turno 

        historico_partidas.append((tabuleiro, historico_jogo))

    salvar_resultado(nome_jogador1, nome_jogador2, placar, historico_partidas)
    print("Jogo finalizado! Placar e histórico salvos.")

if __name__ == '__main__':
    main()
