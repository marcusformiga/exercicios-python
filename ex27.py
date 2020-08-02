cont = soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        cont += 1
        soma += c
print(f'A soma entre os números impares e multiplos de 3 é {soma}')
print(f'Ao todo {cont} numeros sao impares e multipls de 3 ao mesmo tempo')