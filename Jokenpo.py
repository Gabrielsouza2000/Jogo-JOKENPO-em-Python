import random

def valida_int(Pergunta, min, Max):
   x = int(input(Pergunta))
   while((x < min) or (x > Max)):
      x = int(input(Pergunta))
   return x


def vencedor(jogador1, jogador2):
   global empate, v1, v2
   if jogador1 == jogador2:
      empate += 1
      return "Essa rodada empatou"
   elif jogador1 == 1:  # Pedra
      if jogador2 == 2:  # Papel
         v2 += 1
         return "Jogador 2 venceu esta rodada"
      elif jogador2 == 3:  # Tesoura
         v1 += 1
         return "Jogador 1 venceu esta rodada"
   elif jogador1 == 2:  # Papel
      if jogador2 == 3:  # Tesoura
         v2 += 1
         return "Jogador 2 venceu esta rodada"
      elif jogador2 == 1:  # Pedra
         v1 += 1
         return "Jogador 1 venceu esta rodada"
   elif jogador1 == 3:  # Tesoura
      if jogador2 == 1:  # Pedra
         v2 += 1
         return "Jogador 2 venceu esta rodada"
      elif jogador2 == 2:  # Papel
         v1 += 1
         return "Jogador 1 venceu esta rodada"

# Programa principal
mapeamento_nomes = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}

print('JOKENPO')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('0 - Para fechar o jogos e visualizar o resultado final!')

resultado = []
jogadas = []  # inicializa a lista de jogadas
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escolha sua jogada:', 0, 3)
    if not j1:
        break

    j2 = random.randint(1, 3)
    jogadas.append([j1, j2])

    print(f'Jogador 1 escolheu {mapeamento_nomes[j1]}, Jogador 2 escolheu {mapeamento_nomes[j2]}.')

    # Verifica o resultado da rodada atual
    resultado_rodada = vencedor(j1, j2)
    print(resultado_rodada)  # Aqui é onde você adiciona a exibição do resultado da rodada

for jogada in jogadas:
    for dado in jogada:
        print(dado, end=' ')
    print()

print('numero de vitorias do jogador 1: {}'. format(v1))
print('numero de vitorias do jogador 2: {}'. format(v2))
print('numero de vitorias do empate  : {}'. format(empate))