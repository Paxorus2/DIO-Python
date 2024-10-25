# Operadores Aritméticos
numero1 = float(input("Digite um número: "))
numero2 = float(input("Entre com outro número: "))

# Calculo dos valores

soma = numero1 + numero2    # Soma dois valores
sub = numero1 - numero2     # Subtrai o segundo valor do primeiro
mult = numero1 * numero2    # Multiplica dois valores
div = numero1 / numero2     # Divide o primeiro valor pelo segundo 
resto = numero1 % numero2   # Retorna o resto da divisão do primeiro valor pelo segundo
divint = numero1 // numero2 # Divide o primeiro valor pelo segundo e retorna o quociente inteiro
exp = numero1 ** numero2    # Eleva o primeiro valor à potência do segundo valor
 
# Exibi os valores
print()
print("#" * 5, "RESULTADO DOS VALORES CALCULADOS", "#" * 5)

print(f"Soma: {soma:.2f}")
print(f"Subtração: {sub:.2f}")
print(f"Multiplicação: {mult:.2f}")
print(f"Divisão: {div:.2f}", div)
print(f"Resto da Divisão: {resto:.2f}")
print(f"Divisão Inteira: {divint:.2f}")
print(f"Exponenciação: {exp:.2f}")