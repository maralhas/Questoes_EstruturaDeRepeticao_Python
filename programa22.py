numero = int(input("Verificar numeros primos "))
validador = 0
divisivel = []

for i in range(2, numero):
    if (numero % i ==  0):
        divisivel.append(i)
        validador += 1

if(validador == 0):
     print(f'O número {numero} é primo!')
else:
    print(f'O número {numero} não é primo, porem é divisível por {divisivel}')