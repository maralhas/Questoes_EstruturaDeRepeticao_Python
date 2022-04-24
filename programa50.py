#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

entrada = int(input('Informe o valor de N: '))

print ('H= 1 +', end = '')
n = h = 1

for i in range(1, entrada +1 ):
    print(f' 1 / {n+1}', end = '')
    if i < entrada:
        if i == entrada -1:
            print('.')
            break
        else:
            print(' + ', end = '')
    n += 1

for i in range(1, entrada +1):
    h += 1 / i
    if i == entrada:
        h -=1
print(f'A soma da série deu {h:.2f}')