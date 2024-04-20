vogais = "aeiouAEIOU"
palavra = input("Insira uma palavra: ")
total_vogais = 0

for letra in palavra: 
    # Verificando se a letra da palavra se encontra dentro da variavel 'vogais'
    if letra in vogais: 
        print(f"Vogal encontrada na {palavra.index(letra) + 1}ª letra da palavra")
        total_vogais += 1 # Somando vogais a cada vez encontrada

print(f"Existem {total_vogais} vogais na palavra {palavra}")