
base = int(input('Digite a base: '))
espoente = int(input('Digite a espoente: '))
result = base

for i in range(1, espoente):
    result *= base

print(f'O resultado é: {result}')
