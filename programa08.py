soma = float(input('Digite um numero: '))

for n in range(2,6):
    soma += float(input('Digite um numero: '))
    media = soma / n
    print(f'A soma dos numeros é: {soma} e a media: {media}')