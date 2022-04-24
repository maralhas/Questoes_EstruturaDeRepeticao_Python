while True:
    try:
        numero = int(input('Informe um número inteiro: '))
    except ValueError:
        print('Informe apenas numeros inteiros.')
    else:
        numero = str(numero)[::-1]
        break
print(numero)