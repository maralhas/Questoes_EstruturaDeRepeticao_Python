maximo = float(input('Digite um número: '))

for _ in range(5):
    maximo = max(maximo, float(input('Digite um número: ')))
    print(f'Número áximo encontrado até agora é : {maximo}')