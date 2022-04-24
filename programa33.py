import math
temperaturas = []
minima = maxima = media = temperatura = 0.0

print('Digite x para sair')
while True:

    entrada = input('Digite a temperatura: ')
    if entrada == 'x':
        break
    else:
        temperaturas.append(float(entrada))

soma_das_teperaturas = sum(temperaturas)
maxima = max(temperaturas)
minima = min(temperaturas)
media = (soma_das_teperaturas / len(temperaturas))

print(f'A maior temperatura informada foi: {maxima}')
print(f'A menor temperatura informada foi: {minima}')
print(f'A media das temperaturs é: {media}')