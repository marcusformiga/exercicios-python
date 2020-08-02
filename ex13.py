cumprimento = float(input('Informe o cumprimento do terreno em metros: '))
largura = float(input('Informe a largura do terreno em metros: '))
area = cumprimento * largura
cercaM = 5
gasto = area * cercaM
print(f'Um terreno de {cumprimento}m x {largura}m tem área de {area}m² e você vai gastar {gasto} reais para colocar cerca no terreno.')