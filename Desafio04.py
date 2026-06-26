#Desafio 4 – Análise de Produtos
#Objetivo:
#Aprender a trabalhar com dicionários.

produtos = {
    "Notebook": 3500,
    "Mouse": 80,
    "Teclado": 150,
    "Monitor": 1200,
    "Headset": 250
}

#Tarefas:
#1.Exiba todos os produtos e preços.
for produto, preco in produtos.items():
    print(f"O produto {produto} tem o preço de {preco} reais")

#2.Identifique o produto mais caro.
maisCaro = max(produtos, key=produtos.get)
print(f"O produto mais caro é: {maisCaro}")

#3.Identifique o produto mais barato.
maisBarato = min(produtos, key=produtos.get)
print(f"O produto mais barato é: {maisBarato}")

#4.Calcule o valor médio dos produtos.

Media = sum(produtos.values()) / len(produtos)
print('O valor medio dos produtos é:', Media)

#5.Liste os produtos com preço acima de R$ 500.