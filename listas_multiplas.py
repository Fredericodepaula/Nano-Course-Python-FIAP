equipamentos = []
valor = []
numero_serial = []
departamento = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Digite o equipamento: "))
    valor.append(float(input("DIgite o valor: ")))
    numero_serial.append(int(input("Digite o numero de série: ")))
    departamento.append(input("Digite o departamento: "))
    resposta=(input("Digite \"S\" para continuar adicionando equipamentos: ")) .upper()

for indice in range(0,len(equipamentos)):
    print(f"equipamento {indice + 1}:" )
    print(equipamentos[indice])
    print(valor[indice])
    print(numero_serial[indice])
    print(departamento[indice])