
first_numero = int(input('Digite o primeiro número: '))
second_numero = int(input('Digite o segundo número: '))
soma = 0

for i in range(first_numero, second_numero +1):
    soma += i
    print(i)

print(f'A soma de todos os numeros é: {soma}')