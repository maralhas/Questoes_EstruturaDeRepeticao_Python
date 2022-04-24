numero = int(input('Digite um número: '))
fatorial = []
resultado = 1

for i in range(numero):
    fatorial.append(numero - i)
    resultado *= fatorial[i]
print(resultado)