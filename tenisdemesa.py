import random


# função para ler apenas números
def ler_numero(msg):

    while True:
        valor = input(msg)

        if valor.isdigit():
            return int(valor)
        else:
            print("Digite um número válido!")


# função para ler os sets e evitar empate
def ler_sets_partida(j1, j2): 

    while True:

        s1 = ler_numero("Sets de " + j1 + ": ")
        s2 = ler_numero("Sets de " + j2 + ": ")

        # impede 0x0
        if s1 == 0 and s2 == 0:
            print("Não pode 0 x 0! Digite novamente.")

        # impede empate
        elif s1 == s2:
            print("Não pode empate! Alguém precisa vencer.")

        else:
            return s1, s2


# função para cadastrar jogadores
def cadastrar_jogadores():

    print("\nBem vindos, prontos?")
    print("Coloquem seus nomes!")

    jogadores = []

    for i in range(5):
        nome = input("Jogador " + str(i+1) + ": ")
        jogadores.append(nome)

    print("Boa sorte no campeonato!")

    return jogadores


# função que controla as partidas
def jogar_partidas(jogadores):

    pontos = {}
    sets_ganhos = {}
    sets_perdidos = {}
    partidas_jogadas = {}

    # inicializa tudo com 0
    for j in jogadores:
        pontos[j] = 0
        sets_ganhos[j] = 0
        sets_perdidos[j] = 0
        partidas_jogadas[j] = 0

    print("\n--- Partidas ---")

    i = 0

    while True:

        disponiveis = []

        # pega quem jogou menos de 2 partidas
        for j in jogadores:
            if partidas_jogadas[j] < 2:
                disponiveis.append(j)

        # se não tiver 2 jogadores, para
        if len(disponiveis) < 2:
            break

        # sorteio da partida
        j1, j2 = random.sample(disponiveis, 2)

        print("\nPartida " + str(i+1))
        print(j1 + " x " + j2)

        # leitura segura do placar
        s1, s2 = ler_sets_partida(j1, j2)

        # Sets ganhos - sets perdidos
        sets_ganhos[j1] += s1
        sets_ganhos[j2] += s2

        sets_perdidos[j1] += s2
        sets_perdidos[j2] += s1

        # atualiza partidas jogadas
        partidas_jogadas[j1] += 1
        partidas_jogadas[j2] += 1

        # define vencedor
        if s1 > s2:
            pontos[j1] += 1
        else:
            pontos[j2] += 1

        i += 1

    return pontos, sets_ganhos, sets_perdidos


# função de desempate (CORRIGIDA)
def resolver_empates(pontos, sets_ganhos, sets_perdidos):

    print("\n--- Desempate ---")

    jogadores = list(pontos.keys())

    for i in range(len(jogadores)):
        for j in range(i+1, len(jogadores)):

            j1 = jogadores[i]
            j2 = jogadores[j]

            # calcula saldo
            saldo1 = sets_ganhos[j1] - sets_perdidos[j1]
            saldo2 = sets_ganhos[j2] - sets_perdidos[j2]

            # só desempata se TODOS os critérios forem iguais
            if (pontos[j1] == pontos[j2] and
                saldo1 == saldo2 and
                sets_ganhos[j1] == sets_ganhos[j2]):

                print("\nDesempate REAL: " + j1 + " x " + j2)

                s1, s2 = ler_sets_partida(j1, j2)

                # atualiza sets
                sets_ganhos[j1] += s1
                sets_ganhos[j2] += s2

                sets_perdidos[j1] += s2
                sets_perdidos[j2] += s1

                # atualiza pontos
                if s1 > s2:
                    pontos[j1] += 1
                else:
                    pontos[j2] += 1


# função para mostrar ranking + campeão
def mostrar_ranking(pontos, sets_ganhos, sets_perdidos):

    ranking = []

    for jogador in pontos:

        saldo = sets_ganhos[jogador] - sets_perdidos[jogador]

        ranking.append([jogador, pontos[jogador], saldo, sets_ganhos[jogador]])

    # ordena ranking
    ranking.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

    print("\n--- Ranking Final ---")

    for i in range(len(ranking)):

        nome = ranking[i][0]
        pts = ranking[i][1]
        saldo = ranking[i][2]

        print(str(i+1) + " - " + nome + " | pontos: " + str(pts) + " | saldo: " + str(saldo))

    # destaque do campeão
    campeao = ranking[0][0]
    print("\n🏆 CAMPEÃO:", campeao)

    # top 3
    print("\n--- Pódio ---")
    for i in range(3):
        print(str(i+1) + "º lugar:", ranking[i][0])


# programa principal

while True:
    jogadores = cadastrar_jogadores()

    pontos, sets_ganhos, sets_perdidos = jogar_partidas(jogadores)

    resolver_empates(pontos, sets_ganhos, sets_perdidos)

    mostrar_ranking(pontos, sets_ganhos, sets_perdidos)