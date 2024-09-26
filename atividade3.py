numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero % 2 == 0:  #resto de divisão de 2, se for igual a 0 é par se não for é impar
        print(f"numeros pares: {numero}")
    else:
        print(f"numeros impares: {numero}")