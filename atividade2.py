a = 4
b = 2

def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "erro: divisao por zero"

resultado = divisao(a,b)
print(resultado)