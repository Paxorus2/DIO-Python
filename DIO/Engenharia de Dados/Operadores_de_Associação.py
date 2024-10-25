"""
Os operadores de associação em Python são usados 
para verificar se um valor está presente em uma 
sequência, como uma lista, tupla ou string.
Existem dois operadores principais de associação:
in: Verifica se um valor está presente em uma sequência.
not in: Verifica se um valor não está presente em uma sequência.

Esses operadores são muito úteis para validar a 
presença de elementos em coleções e podem ser 
usados em diversas situações
"""

# Exemplo com 'in'
frutas = ["maçã", "banana", "laranja"]
print("maçã" in frutas)         # Saída: True

# Exemplo com 'not in'
print("uva" not in frutas)      # Saída: True

# Exemplo2 com 'in'
print("Pera" in frutas)         # Saída: False

# Exemplo2 com 'not in'
print("Banana" not in frutas)   # Saída: True