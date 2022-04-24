intervalo_0_25 = intervalo_26_50 = intervalo_51_75 = intervalo_76_100 = 0 
while True:
    try:
        entrada = int(input('Digite um numero:'))
    except:
        print('Digite atenas numeros inteiros, caso deseje terminar com a entrada informe um numero negativo.')
    else:
        if entrada < 0:
            break
        elif entrada >= 0 and entrada <= 25:
            intervalo_0_25 += 1
        elif entrada >= 26 and entrada <= 50:
            intervalo_26_50 += 1
        elif entrada >= 51 and entrada <= 75:
            intervalo_51_75 += 1
        elif entrada >= 76 and entrada <= 100:
            intervalo_76_100 += 1

print(f'Foram digitatados {intervalo_0_25} no intervalo de [0-25]')
print(f'Foram digitatados {intervalo_26_50} no intervalo de [26-50]')
print(f'Foram digitatados {intervalo_51_75} no intervalo de [51-75]')
print(f'Foram digitatados {intervalo_76_100} no intervalo de [76-100]')        