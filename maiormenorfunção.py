def maior_menor(a, b):

    if a > b:
        return f'O numéro {a} é maior que o número {b}'
    elif a == b:
        return f'O número {a} é igual ao número {b}'
    return f'O número {a} é menor que o número {b}'

a = int(input('Informe um número:'))
b = int(input('Informe um número:'))
print(maior_menor(a, b))