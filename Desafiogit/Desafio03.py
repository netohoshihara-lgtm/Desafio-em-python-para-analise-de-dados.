#Desafio 3 – Análise de Notas
#Objetivo:
#Praticar condições e cálculos estatísticos básicos.

notas = [7.5, 8.0, 5.5, 9.0, 6.5, 10.0, 4.5, 8.5]

#Tarefas:
#1.Calcule a média da turma.
media = sum(notas) / len(notas)
print('A média da turma é:', media)

#2.Conte quantos alunos foram aprovados (nota ≥ 7).
aprovados = len([apro for apro in notas if apro >=7])
print(aprovados,'Alunos foram aprovados')

#3.Conte quantos alunos foram reprovados.
reprovados = len([repro for repro in notas if repro <7])
print(reprovados, 'Alunos foram reprovados')

#4.Mostre a porcentagem de aprovação.
percentual_aprovados = aprovados / len(notas) * 100
print(percentual_aprovados,'Porcento foram aprovados')

