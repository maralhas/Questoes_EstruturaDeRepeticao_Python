numeros = []
par = impar = 0

for i in range (10):
    numero = int(input('Digite um numero: '))
    numeros.append(numero)

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'A quantidade de numero par é de: {par}')
print(f'A quantidade de numero ímpar é de: {impar}')