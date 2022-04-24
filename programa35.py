entrada = int(input('Digite um número: '))
numeros_primos = []

for i in range(entrada +1):
    if i % 2 == 1 and i != 2:
        numeros_primos.append(i)

print(f'Os numeros primos são: {numeros_primos}')