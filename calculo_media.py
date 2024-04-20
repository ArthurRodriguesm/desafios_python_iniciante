length_list = int(input("Insira a quantidade de números que terá na lista: "))
list_numbers = []

for count in range(0, length_list): # Gerando looping para adicionar números de acordo com tamanho da lista informada
    number = int(input(f"Número {count}: ")) # Solicitando número ao usuário
    list_numbers.insert(count, number) # Inserindo número do usuário na lista
    result_sum = sum(list_numbers)

result = float(result_sum / len(list_numbers)) # Calculando média dos valores inseridos na lista

print(f"Média: {result}")