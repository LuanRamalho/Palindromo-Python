word = input("Digite uma palavra qualquer. ")
if str(word) == str(word)[::-1]:
    print(word)
    print("Essa palavra é Palíndromo")
else:
    print(word)
    print("Essa palavra não é Palíndromo")
