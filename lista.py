equipamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    equipamentos.append(float(input("Valor: ")))
    equipamentos.append(input("Departamento: "))
    resposta=input("Digite \"S\" para continuar") .upper()

for elementos in equipamentos:
    print(elementos)