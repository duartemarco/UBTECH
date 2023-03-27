# Q2) Escreva uma função que receba dois números e retorne true se o primeiro número for múltiplo do segundo

def multiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

print("9 é múltiplo de 3?")
print(multiplo(9, 3)) # esperado True

print("8 é múltiplo de 3?")
print(multiplo(8, 3))
