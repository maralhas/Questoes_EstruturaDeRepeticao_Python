
numeros = []

while True:
    numero = int(input('Digite um numero de 0 a 1000: '))
    if 0 <= numero <= 1000:
        numeros.append(numero)
    else:
        print('Não informou um valor válido:')

    opc = input('Digite S para Sair ou precione qual quer tecla pra continuar')
    opc =  opc.upper()
    if opc == 'S':
        break
maximo = max(numeros)
minimo = min(numeros)
print(f'O menor numero encontrado foi {minimo} e o mair foi {maximo} a soma dos dois é {minimo + maximo}')