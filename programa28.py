valor_total_estimado = media = 0.0

while True:
    try:
        quantidade_de_cds = int(input("Informe a quantidade de CD's: "))
    except:
        print("Informe somente números inteiros: ")
    else:
        break

for i in range(quantidade_de_cds):
    while True:
        try:
            valor = float(input("Informe o preço de cada um deles: "))
        except:
            print("Informe somente números reais: ")
        else:
            valor_total_estimado += valor
            break

media = valor_total_estimado / quantidade_de_cds

print(f'O valor infestido é de: {valor_total_estimado} e a media pega por cada CD é de: {media}')