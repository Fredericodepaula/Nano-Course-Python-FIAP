# Exercício 1:

def media(n1,n2):
    resultado = (n1 + n2) / 2
    print(f"A média de {n1} e {n2} é = {resultado}")

media(8,6)

# Exercício 2:

def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} é par!!")
    else:
        print(f"{numero} é impar!!")

par_ou_impar(2)

# Exercício 3:

def calculadora(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b 
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b != 0:
            return a / b 
        else:
            return "Divisão por 0 são invalidas"
    else:
        return "Operação Invalida"
    
print("Soma:", calculadora(10, 5, "+"))
print("Subtração:", calculadora(10, 5, "-"))
print("Multiplicação:", calculadora(10, 5, "*"))
print("Divisão:", calculadora(10, 0, "/"))

# Exercício 4:

def maior(a, b, c):
    return max(a, b, c)

print(f"{maior(10,5,7)} é o maior número")