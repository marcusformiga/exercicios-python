from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('Olá, sou seu computador, vamos jogar um jogo ?')
print('Ele se chama PEDRA, PAPEL OU TESOURA. Conhece as regras não é ?')
computador = randint(0, 2)
print("""
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
print('-=-' *30)
jogador = int(input('Qual é a sua opção ?'))
if jogador == 0 and computador == 0:
    print(f'Você escolheu {itens[jogador]} e o computador {itens[computador]}, EMPATE')
elif jogador == 0 and computador == 1:
    print(f'Você escolheu {itens[jogador]} e o computador {itens[computador]}, VOCÊ PERDEU ! ')
elif jogador == 0 and computador == 2:
    print(f'Você escolheu {itens[jogador]} e o computador {itens[computador]}, VOCÊ GANHOU!')
elif jogador == 1 and computador == 0:
    print(f'Você escolheu {itens[jogador]} e o computador {itens[computador]}, VOCÊ GANHOU!')
elif jogador == 1 and computador == 1:
    print(f'Você escolheu {itens[jogador]} e o computador {itens[computador]}, EMPATE!')
elif jogador == 1 and computador == 2:
    print(f'Você escolheu {itens[jogador]} e o computador {itens[computador]}, VOCÊ PERDEU!')
elif jogador == 2 and computador == 0:
    print(f'Você escolheu {itens[jogador]} e o computador {itens[computador]}, VOCÊ GANHOU!')
elif jogador == 2 and computador == 1:
    print(f'Você escolheu {itens[jogador]} e o computador {itens[computador]}, VOCÊ PERDEU!')
elif jogador == 2 and computador == 2:
    print(f'Você escolheu {itens[jogador]} e o computador {itens[computador]}, EMPATE!')

