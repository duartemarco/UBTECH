# Q1) Faça uma função que retorne o maior de dois números:

# printando os resultados (print)
"""def maximo_print(num1, num2):
    if num1 > num2:
        print(num1)
    #else:
        print(num2)"""

# retornando os resultados (return)
def maximo(num1, num2):
    if num1 > num2:
        resultado = num1
    else:
        resultado = num2
    return resultado

print(maximo(5,6), maximo(2,1), maximo(7,7))

maximo(5,6)
maximo(2,1)
maximo(7,7)
