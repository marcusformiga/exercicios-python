from random import randint
print('Olá sou seu computador')
print('Acabei de pensar um número entre 0 e 10, será que você consegue adivinhar o número?')
computador = randint(0, 10)
jogador = int(input('Tente acertar o número ....'))
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Tente acertar o número'))
    if jogador == computador:
        acertou = True
        tentativas += 1
    else:
        if jogador < computador:
            print('Um pouco mais')
        elif jogador > computador:
            print('Um pouco menos')
print(f'Acertou com {tentativas} palpites')
