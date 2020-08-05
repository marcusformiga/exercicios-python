def volume_cilindro(altura, raio):
    volume = 3.14 * raio**2 * altura
    return f'O volume do cilindro é de {volume:.2f}m³'


altura = float(input('Informe a altura do cilindro'))
raio = float(input('Informe o raio do cilindro'))
print(volume_cilindro(altura, raio))