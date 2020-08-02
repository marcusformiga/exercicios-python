frase = str(input('Digite uma frase: ')).upper().strip()
frase2 = frase[:: -1]
if frase == frase2:
    print(f'A frase {frase} é um palindromo')
else:
    print(f'A frase {frase} não é um palindromo')