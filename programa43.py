cachorro_quente = bauru_Simples = bauru_com_ovo = hamburguer = cheeseburguer = refrigerante = 0
quantidade_cachorro_quente = quantidade_bauru_Simples = quantidade_bauru_com_ovo = quantidade_hamburguer = quantidade_cheeseburguer = quantidade_refrigerante = 0
precos = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00]

print(''' Especificação   Código  Preço
 Cachorro Quente 100     R$ 1,20
 Bauru Simples   101     R$ 1,30
 Bauru com ovo   102     R$ 1,50
 Hambúrguer      103     R$ 1,20
 Cheeseburguer   104     R$ 1,30
 Refrigerante    105     R$ 1,00 ''')

print('Digite o código 0 para finalizar o pedido')
while True:
    try:
        entrada = int(input('Digite o Codigo do pedido: '))
        if entrada == 0:
            print(bauru_Simples)
            break
    except ValueError:
        print('Indorme apenas números inteiros. ')
    else:
        if entrada == 100:
            quantidade_cachorro_quente += int(input('Digite a quantidade: '))
            total_cachorro_quente = quantidade_cachorro_quente * precos[0]

        if entrada == 101:
            quantidade_bauru_Simples += int(input('Digite a quantidade: '))
            total_bauru_Simples = quantidade_bauru_Simples * precos[1]
        
        if entrada == 102:
            quantidade_bauru_com_ovo += int(input('Digite a quantidade: '))
            total_bauru_com_ovo = quantidade_bauru_com_ovo * precos[2]
        
        if entrada == 103:
            quantidade_hamburguer += int(input('Digite a quantidade: '))
            total_hamburguer = quantidade_hamburguer * precos[3] 
        
        if entrada == 104:
            quantidade_cheeseburguer += int(input('Digite a quantidade: '))
            total_cheeseburguer = quantidade_cheeseburguer * precos[4]

        if entrada == 105:
            quantidade_refrigerante += int(input('Digite a quantidade: '))
            total_refrigerante = quantidade_refrigerante * precos[5]

total = (total_cachorro_quente + total_bauru_Simples + total_bauru_com_ovo + total_hamburguer + total_cheeseburguer + total_refrigerante)

print('Quantidade       Produto     Preço       total')
if quantidade_cachorro_quente > 0:
    print(f'{quantidade_cachorro_quente}    Cachorro Quente     {precos[0]}         {total_cachorro_quente}')
if quantidade_bauru_Simples > 0:
    print(f'{quantidade_bauru_Simples}    Bauru Simples     {precos[1]}         {total_bauru_Simples}')
if quantidade_bauru_com_ovo > 0:
    print(f'{quantidade_bauru_com_ovo}    Bauru com Ovo     {precos[2]}         {total_bauru_com_ovo}')
if quantidade_hamburguer > 0:
    print(f'{quantidade_hamburguer}    Hamburguer           {precos[3]}         {total_hamburguer}')
if quantidade_cheeseburguer > 0:
    print(f'{quantidade_cheeseburguer}    Cheeseburguer     {precos[4]}         {total_cheeseburguer}')
if quantidade_refrigerante > 0:
    print(f'{quantidade_refrigerante}    Refrigerante     {precos[5]}         {total_refrigerante}')
print(f'Total do pedido {total}')
