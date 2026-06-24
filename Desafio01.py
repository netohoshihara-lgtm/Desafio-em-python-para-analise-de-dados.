#Desafio 1 – Análise de Vendas
#Objetivo:
#Praticar listas, loops e funções básicas (sum(), max(), min(), len()).
 
#lista com as vendas de uma loja durante 10 dias:
vendas = [120, 250, 180, 300, 150, 400, 220, 190, 350, 280]

#Tarefas:
#1. Calcule o total de vendas.
total_de_vendas = sum(vendas)
print('O total de vendas é:',total_de_vendas)

#2. Calcule a média de vendas.
media_de_vendas = sum(vendas) /len(vendas)
print('A média de vendas é:', media_de_vendas)

#3. Descubra a maior venda.
maior_venda = max(vendas)
print('A maior venda efetuada é:',maior_venda)

#4. Descubra a menor venda.
menor_venda = min(vendas)
print('A menor venda efetuada é:', menor_venda)

#5. Mostre quantos dias tiveram vendas acima de R$ 250.
dias_acima = len([acima for acima in vendas if acima >250])
print('Este é o total de vendas acima de 250:', dias_acima)
