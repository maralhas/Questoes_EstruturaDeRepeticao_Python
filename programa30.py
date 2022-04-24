print('Panificadora Pão de Ontem - Tabela de preços')
preco = 0.18
for quantidade in range (1, 51):
    print('{:.0f}'.format(quantidade) + ' - R${:.2f}'.format(preco * quantidade))