inventario = []
resposta = "S"

while resposta == "S":
    equipamento=[(input("Equipamento: ")),
                 float(input("Valor: ")),
                 int(input("Número de série: ")),
                 input("Departamento: ")]
    inventario.append(equipamento)
    resposta=input("Digite \"S\" para continuar inserindo equipamentos: ").upper()

for elemento in inventario:
    print("Nome:", elemento[0])
    print("Valor:", elemento[1])
    print("Número de série:", elemento[2])
    print("Departamento:", elemento[3])

busca = input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca==elemento[0]:
        print("Valor:", elemento[1])
        print("Número de Série:", elemento[2])

deprecicao=input("DIgite o equipamento que será depreciado: ")
for elemento in inventario:
    if deprecicao == elemento[0]:
        print("Valor antigo:", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Valor depreciado:", elemento[1])




