jose = joao = luiz = ian = nulo = branco = 0
votos = []
while True:
    try:
        entrada = int(input('Digite o numero do candidato: '))
        if entrada == 0:
            break
    except ValueError:
        print('Informe um numero Inteiro.')
    else:
        if entrada == 1:
            print('Cadidato: Jose')
            jose += 1
        elif entrada == 2:
            print('Cadidato: Jão')
            joao += 1
        elif  entrada == 3:
            print('Cadidato: Luiz')
            luiz += 1
        elif entrada == 4:
            print('Cadidato: Ian')
            ian += 1
        elif entrada == 5:
            print('Voto Anulado')
            nulo += 1
        elif entrada == 6:
            print('Voltou Branco')
            branco += 1

votos.append(jose)
votos.append(joao)
votos.append(luiz)
votos.append(ian)
votos.append(nulo)
votos.append(branco)
total_de_votos = sum(votos)
percetual_votos_nulos = ((votos[4] * 100) / total_de_votos)
percetual_votos_brancos = ((votos[5] * 100) / total_de_votos)

for i in range(0, 6):
    if i <= 3:
        print(f'Cadidato {i +1}: recebeu {votos[i]}')
    elif i == 4:
        print(f'O todal de votos nulos foi de : {votos[4]}')
    elif i == 5: 
        print(f'O todal de votos Brancos foi de : {votos[5]}')
print(f'Quantidade total de votos: {total_de_votos}')
print('Percentual de votos nulos é de {:.2f}'.format(percetual_votos_nulos))    
print('Percentual de votos nulos é de {:.2f}'.format(percetual_votos_brancos))
