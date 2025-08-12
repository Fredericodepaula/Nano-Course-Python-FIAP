equipamentos = []
valores = []
numeros_seriais = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Digite o nome do equipamento: "))
    valores.append(float(input("Digite o valor do equipamento: ")))
    numeros_seriais.append(int(input("Digite o número de série do equipamento: ")))
    resposta = (input("Digite \"S\" para continuar: ")).upper()


busca=input("Digite o nome do Equipamento para buscar: ")
for i in range(0,len(equipamentos)):
    if busca==equipamentos[i]:
        print(f"Valor: {valores[i]}")
        print(f"Número de série: {numeros_seriais[i]}")

