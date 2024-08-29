
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")


num1 = float(num1)
num2 = float(num2)


operacao = input("Escolha a operação (+, -, *, /): ")


if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:  
        resultado = num1 / num2
    else:
        resultado = "Divisão por zero não é permitida."
else:
    resultado = "Operação inválida."

print(f"O resultado da operação {operacao} é: {resultado}")