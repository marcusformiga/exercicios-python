n1 = int(input('Informe um número:'))
n2 = int(input('Informe um número:'))
if n1 >= 0 or n2>= 0:
    raiz = n1 * (1/2)
    raiz1 = n2 * (1/2)
    print(f'A raiz quadrada de {n1} é {raiz}')
    print(f'A raiz quadrada de {n2} é {raiz1}')
else:
    print('Não existe raíz inteira para o número')