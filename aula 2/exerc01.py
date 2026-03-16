# Estrutura de condição
# IF e ELSE e ELIF

# Entrada
# Variavel + Conversão de Tipo(Float) + Entrada de Dados(Input)
media = float(input("Digite sua média: "))

# Processamneto
if media < 6:
    if media >= 3:
        print("Exame Final")
    else:
        print("Reprovado")
else:
    print("Aprovado")
