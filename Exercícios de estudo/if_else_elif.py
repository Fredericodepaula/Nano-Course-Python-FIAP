# Exercício 01:

idade= 18

if idade< 18:
    print("menor de idade")

elif idade == 18:
    print("Voce tem 18 anos")

else:
    print("maior que 18 anos")

# Exercício 02:

numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# Exercício 03:

nota1=float(input("Digite sua nota 1: "))
nota2=float(input("Digite sua nota 2: "))

media= (nota1+nota2) /2

if media >= 6:
    print("Aprovado")

elif media>5:
    print("Recuperação")

else:
    print("Reprovado")

# Exercício 04:

senha= 1358
tentativa=int(input("Digite a senha: "))

if senha == tentativa:
    print("Acesso autorizado")

else:
    print("Acesso negado")

# Exercício 05:

temperatura=int(input("Digite a temperatura em graus: "))

if temperatura<0:
    print("Congelando")

elif temperatura<=20:
    print("Frio")

elif temperatura<=30:
    print("Agradável")

else:
    print("Quente")

