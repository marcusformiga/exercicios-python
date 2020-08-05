def area (larg, comp):
    areaTerreno = larg * comp
    print(f'Um terreno com {larg}m de largura e {comp}m de comprimento possui área de {areaTerreno}m²')


larg = float(input('Informe a largura do terreno(m):'))
comp = float(input('Informe o comprimento do terreno (m):'))

area(larg, comp)
