print('Digite -1 para parar com as entras de notas.')
contador = 0
soma_de_notas = 0
while True:
    nota = input('Digite uma nota: ')
    if nota == '-1':
        break
    else:
        contador += 1
        soma_de_notas += float(nota)

media = soma_de_notas / contador
print(f'A média aritimpetica é de: {media}')
