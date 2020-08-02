total = 0
numero = int(input('Digite um número: '))
for cont in range(1, numero + 1):
   if numero % cont == 0:
       total += 1
   else:
       print('')
if total == 2:
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo! ')