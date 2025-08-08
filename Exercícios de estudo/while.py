# Exercício 1:

senha=("python123")
tentativa=input("Digite a senha: ")

while tentativa != senha:
    print("Senha incorreta")
    tentativa=input("Digite a senha: ")

print("Acesso liberado")

# Exercício 2:

numero=1

while numero<=10:
    print(numero)
    numero += 1

# Exercício 3:

numero = int(input("Digite um número para ver sua tabuada: "))
multiplicador=1

while multiplicador<=10:
    print(f"{numero} x {multiplicador} = {numero* multiplicador}")
    multiplicador +=1 

# Exercício 4:

numero_secreto= 8
tentativa=int(input("Adivinhe o número secreto (De 1 até 10): "))

while numero_secreto != tentativa:
    print("Você errou! Tente Novamente")
    tentativa=int(input("Adivinhe o número secreto (De 1 até 10): "))

print("Parabéns você acertou!!!")


