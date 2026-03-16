# Estrutura de condição
# IF e ELSE e ELIF 2

# Entrada
# Variavel + Conversão de Tipo(Float) + Entrada de Dados(Input)
media = float(input("Digite sua média: "))

# Processamneto
if media >= 6:
    print("Aprovado")
else:
    if media >= 3:
        print("Exame Final")
    else:
        print("Reprovado")