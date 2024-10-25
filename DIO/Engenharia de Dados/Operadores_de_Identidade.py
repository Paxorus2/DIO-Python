# Variáveis
a = [1, 2, 3]
b = a
c = [1, 2, 3]


print(a is b)       # True, porque b é o mesmo objeto que a
print(a is c)       # False, porque c é um objeto diferente, embora tenha o mesmo conteúdo
print(a is not c)   # True, porque c não é o mesmo objeto que a
print(b is c)       # False, porque b não é o mesmo objeto que c