entrada = input("[E] para entrar e [S] para psssar: ")
senha_digitada = input("digite a Senha: ")
senha = "12345678"

if(entrada == "E" or entrada == "e"):
    if(senha == senha_digitada):
        print("Sucesso, você entrou!")
    else:
        print("Você não entrou, senha INCORRETA! ")
elif(entrada == "S" or entrada == "s"):
    if(senha == senha_digitada):
        print("Sucesso, você passou")
    else:
        print("Voce não passou, senha INCORRETA")
else:
    print("Você não selecionou uma opção valida")