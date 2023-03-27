# Q3) Escreva uma função que receba o lado (L) de um quadrado e retorne sua área (A = lado²)

def area(l):
    return l ** 2

# testando
print("A área de um quadrado cujo lado mede 5m é: ")
print(f"{area(5)}m²") # esperado 25

print("A área de um quadrado cujo lado mede 7,5m é: ")
print(f"{area(7.5)}m²") # esperado 56.25
