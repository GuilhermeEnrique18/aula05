pin = 1234
tentativas = 0
mensagem = "Acesso Bloqueado"
while tentativas < 3:
    senha = int(input("Informe sua senha"))
    if senha == pin:
        mensagem = ("logado")
        break
    tentativas +=1
    print("Senha incorreta")
print(mensagem)