ano = int(input('Informe o ano que deseja saber se é bissexto:'))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 !=0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
