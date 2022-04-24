cantidato_1 = cantidato_2 = cantidato_3 = nulo = 0

while True:
    try:
        numero_total_de_eleitores = int(input('Informe o número de eleitores: '))
    except:
        print('ERRO!! Informe somente números inteiros.')
    else:
        break

print('''Digite:
[1] Para o candidato de numero 1
[2] Para o candidato de numero 2
[3] Para o candidato de numero 3''')

for i in range(numero_total_de_eleitores):
    while True:
        try:
            voto = int(input('Informe o número do candidato: '))
        except:
            print('ERRO!! Informe somente números inteiros.')
        else:
            if voto == 1:
                cantidato_1 += 1
                break
            elif voto == 2:
                cantidato_2 += 1
                break
            elif voto == 3 :
                cantidato_3 += 1
                break
            else:
                nulo += 1
                break
print(f'O canditado 1 recebeu: {cantidato_1} voto(s)')
print(f'O canditado 2 recebeu: {cantidato_2} voto(s)')
print(f'O canditado 3 recebeu: {cantidato_3} voto(s)')
print(f'A quantidade de votos nulos: {nulo}')