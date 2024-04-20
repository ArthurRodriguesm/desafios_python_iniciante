word = str(input("Insira uma palavra: "))
list(word)

reverse_word = word[::-1]

result = "é um Palíndromo!" if word == reverse_word else "não é um Palíndromo!"

print(f"A palavra '{word}' {result}")