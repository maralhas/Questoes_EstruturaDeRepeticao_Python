valor_do_juros = 0
valor_da_parcela = 0
quantidade_de_parcelas = 1
juros = 0
while True:
    try:
        valor_da_divida = float(input('Digite o valor da divida: '))
    except:
        print('Informe apenas numeros.')
    else: 
        valor_da_parcela = valor_da_divida
        break

print('Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela')
for i in range(5):
    if i == 0 :
        print(' {:.2f}       '.format(valor_da_divida)  + '         {:.2f}     '.format(valor_do_juros) + 
        '    {:.0f}'.format(quantidade_de_parcelas) + '           {:.2f}'.format(valor_da_parcela))
        juros = 0.10
        quantidade_de_parcelas = 3
    else:
        valor_do_juros = valor_da_divida * juros
        valor_da_parcela = (valor_da_divida + valor_do_juros) / quantidade_de_parcelas
        print(' {:.2f}       '.format(valor_da_divida + valor_do_juros)  + '         {:.2f}     '.format(valor_do_juros) + 
        '    {:.0f}'.format(quantidade_de_parcelas) + '           {:.2f}'.format(valor_da_parcela))
        juros += 0.05
        quantidade_de_parcelas += 3