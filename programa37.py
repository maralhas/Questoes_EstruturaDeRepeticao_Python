import math
id_cliente = []
altura = []
peso = []

while True:
    
    try:
        cliente =  int(input('Informe a sua matricula: '))
        if cliente == 0:
            break
    except ValueError:
        print('Erro !!! - Informe apenas números Inteiros')
    else:
        id_cliente.append(cliente)

    while True:
        try:
            entrada_autura =  float(input('Informe a sua altura: '))
        except ValueError:
            print('Erro !!! - Informe apenas números Inteiros')
        else:
            altura.append(entrada_autura)
            break
    while True:
        try:
            entrada_peso =  float(input('Informe o seu peso: '))
        except ValueError:
            print('Erro !!! - Informe apenas números Inteiros')
        else:
            peso.append(entrada_peso)
            break

media_altura = sum(altura) / len(altura)
media_peso = sum(peso) / len(peso)
id_mais_alto = altura.index(max(altura))
id_mais_baixo = altura.index(min(altura))
id_maior_peso = peso.index(max(peso))
id_menor_peso = peso.index(min(peso))

print(f'O mais alto é: {id_mais_alto +1}')
print(f'O mais baixo é: {id_mais_baixo +1}')
print(f'O mais gordo é: {id_maior_peso +1}')
print(f'O mais magro é: {id_menor_peso +1}')
print(f'A media de peso é de {media_peso +1} e a de altura {media_altura +1}')