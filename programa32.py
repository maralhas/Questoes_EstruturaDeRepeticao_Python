import math
numero = int(input('Digite o numero que quer realizar a fatorial : '))

fatorial = math.factorial(numero)

print(f'Fatorial de: {numero}')
for i in range(numero - 1): 
    print(numero -i, end= '.')
print (f'1 = {fatorial}')