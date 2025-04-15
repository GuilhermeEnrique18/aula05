i = 0
soma = 0
while i < 10:
    somaNotas = float(input(f"Digite a nota {i+1}: "))
    i+=1
    soma += somaNotas

media = soma/10

print(f"{media:.2f}")
