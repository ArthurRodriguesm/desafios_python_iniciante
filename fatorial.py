number = int(input("Digite um número: "))

def factorial(number):
    if number == 0:
        return 1
    else:
        factorial_result = 1
        for count in range(1, number + 1): # Looping para multiplicar os valores até chegar no número indicado
            factorial_result *= count
        print(f"O fatorial de {number} é {factorial_result}")

factorial(number)