print('Para fechar o programa difite -1')
while True:
    entrada = input ('Digigite um numero: ')
    if entrada == '-1':
        break

    numero = int(entrada)

    if 0 <= numero <= 16:
        fatorial = []
        resultado = 1

        for i in range(numero):
            fatorial.append(numero - i)
            resultado *= fatorial[i]
        print(resultado)