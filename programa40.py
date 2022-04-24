maior = media_veiculos = media = menor_2000 = 0
cod_cidade_maior = cod_cidade_menor = 0
quantidade_de_acidentes = quantidade_de_veiculos = 0
menor = 9999
for i in range (5):
    while True:
        try:
            codigo_da_cidade = int(input('Digite o Codigo da cidade: '))
        except ValueError:
            print('Informe só valores Inteiros.')
        else:
            break    
    while True:
        try:
            quantidade_de_veiculo = int(input('Digite o número de veículos na cidade: '))
        except ValueError:
            print('Informe só valores Inteiros.')
        else:
            quantidade_de_veiculos += quantidade_de_veiculo
            if quantidade_de_veiculo < 2000:
                while True:
                    try:
                        quantidade_de_acidente = int(input('Digite o número de acidentes com vitimas da cidade: '))
                    except ValueError:
                        print('Informe só valores Inteiros.')
                    else:
                        menor_2000 += quantidade_de_acidente
                        media += 1
                        if maior < quantidade_de_acidente / quantidade_de_veiculo:
                            maior = quantidade_de_acidente / quantidade_de_veiculo
                            cod_cidade_maior = codigo_da_cidade
                            break
                        if menor > quantidade_de_acidente / quantidade_de_veiculo:
                            menor = quantidade_de_acidente / quantidade_de_veiculo
                            cod_cidade_menor = codigo_da_cidade
                            break
                        else:
                            break
                break
            else: 
                while True:
                    try:
                      quantidade_de_acidente = int(input('Digite o número de acidentes com vitimas da cidade: '))
                    except ValueError:   
                        print('Informe só valores Inteiros.')     
                    else:
                        quantidade_de_acidentes += quantidade_de_acidente
                        if maior < quantidade_de_acidente / quantidade_de_veiculo:
                            maior = quantidade_de_acidente / quantidade_de_veiculo
                            cod_cidade_maior = codigo_da_cidade
                            break
                        if menor > quantidade_de_acidente / quantidade_de_veiculo:
                            menor = quantidade_de_acidente / quantidade_de_veiculo
                            cod_cidade_menor = codigo_da_cidade
                            break
                        else:
                            break
                break

media_veiculos = quantidade_de_veiculos / 5
print('')

print(f'O número de acidentes com Vitimas é de: {quantidade_de_acidentes + menor_2000}')
print(f'O cod da cidade com o maior indice é {cod_cidade_maior} e o indice é {maior}')
print(f'O cod da cidade com o maior indice é {cod_cidade_menor} e o indice é {menor}')
print(f'A média de veiculos é de: {media_veiculos}')
print(f'a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é de: {menor_2000 / media}')