print('Para fechar o programa difite -1')
while True:
    entrada = input ('Digigite um numero: ')
    if entrada == '-1':
        break

    numero = int(entrada)
    result = 1

    for i in range(1, numero):
        if numero % i == 0:
            result += 1
    if result == 2:
        print(f'O número {numero} é primo!')
    else:
         print(f'O número {numero} não é primo!')