player = dict()
partidas = list()
player['nome'] = str(input('Digite o nome do jogador: '))
total_partidas = int(input(f'Quantas partidas {player["nome"]} jogou?: '))
for c in range(0, total_partidas):
    partidas.append(int(input(f'  Quantos gols fez na partida {c+1}?: ')))
player['gols'] = partidas[:]
player['total'] = sum(partidas)
print('-=' * 30)
print(player)
print('-=' * 30)
for k, v in player.items():
    print(f' O campo {k} tem o valor de {v}')
print('-=' * 30)
print(f' O jogador {player["nome"]} jogou {len(player["gols"])} partidas.')
for i, v in enumerate(player['gols']):
    print(f'    => Na partida {i+1}, fez {v} gols. ')
print(f'Foi um total de {player["total"]} gols.')
print('-=' * 30)


