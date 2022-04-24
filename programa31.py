compra = []
while True:
    try:
        preco_mercadoria =  float(input('Digite o valor da Mercadoria: '))
    except:
        input('ERRO!!! Informe apenas números')
    else:
        if preco_mercadoria == 0:
            break
        else:
            compra.append(preco_mercadoria)

total_da_compra = sum(compra)

print(f'O valor da compra é de R$: {total_da_compra}')

pagamento = float(input('Infome o valor pago pelo cliente: '))
troco = pagamento - total_da_compra

print ('Lojas Tabajara')
for i in range(len(compra)):
    print(f'Produto {i +1}: ' + '{:.2f}'.format(compra[i]))
print(f'Total: {total_da_compra}')
print(f'Dinheiro: {pagamento}')
print(f'Troco: ' + '{:.2f}'.format(pagamento - total_da_compra))