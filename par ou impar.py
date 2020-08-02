from random import randint
print('olá sou seu computador, Vamos jogar par ou ímpar ?')
print('=-=' * 30)
vit = 0
while True:
    jogador = int(input('Digite um valor:'))
    computador = randint(0, 10)
    total = computador + jogador
    tipo =' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou impar. [P/I]')).strip().upper()

    print(f'Você jogou {jogador} e o computador {computador}, total de {total}')
    if tipo == 'P':
       if total % 2 == 0:
        print('Você venceu')
        vit += 1
       else:
           print('Você perdeu')
           break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você venceu')
            vit += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente')
print(f'Você conseguiu vencer {vit} vezes')

