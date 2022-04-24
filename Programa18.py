numeros = [1, 8, 9, 10, 99, 5, -1, 7, 100, 57, 26]
maximo = max(numeros)
minimo = min(numeros)

print(f'O menor numero encontrado foi {minimo} e o mair foi {maximo} a soma dos dois é {minimo + maximo}')

#Resolvendo com for

maior = 0
menor = 1000


for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
    elif numeros[i] < menor:
        menor = numeros[i]
print(f'O menor numero encontrado foi {menor} e o mair foi {maior} a soma dos dois é {menor + maior}')