i = 0
soma = 0
qtdAlunos = int(input("Informe a quantidade de alunos para calcular a media aritmetica da turma: "))
while i < qtdAlunos:
    somaNotas = float(input(f"Digite a nota do aluno {i+1}: "))
    i += 1
    soma += somaNotas

media = soma/qtdAlunos

print(f"{media:.2f}")
