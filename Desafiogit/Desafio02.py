#Desafio 2 – Cadastro de Funcionários
#Objetivo:
#Praticar filtros e compreensão de listas.

#Considere a seguinte lista:
idades = [22, 35, 28, 41, 30, 25, 50, 29]

#Tarefas:
#1.Calcule a idade média.
idade_media = sum(idades) / len(idades)
print('A média de idades é:', idade_media)

#2.Conte quantos funcionários têm mais de 30 anos.
acima_de = len([acima for acima in idades if acima>30])
print(acima_de, 'Funcionarios estão acimda de 30 anos')

#3.Crie uma nova lista contendo apenas funcionários com menos de 30 anos.
abaixo_de = len([abaixo for abaixo in idades if abaixo<30])
print(abaixo_de, 'Funcionarios estão a baixo de 30 anos')

#4.Mostre a idade mais alta e a mais baixa.
maisalta = max(idades)
maisbaixa = min(idades)
print('A idade mais alta é:', maisalta, 'e a idade mais baixa é:',maisbaixa)