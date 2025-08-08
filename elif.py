nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))
doença=input("Você tem alguma doença? Sim ou Não ") .upper()

if idade >=65:
    print("Você tem direito ao atendimento prioritário")

elif doença == "SIM":
    print("Vá para a enfermaria")

else:
    print("Você não possui nenhum atendimento prioritário, aguarde")
