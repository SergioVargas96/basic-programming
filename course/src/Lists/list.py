# Suma de elementos de una lista
numbers = [1, 2, 3, 4, 5, 6]
sum_numbers = sum(numbers)

print("Suma de la lista: ", sum_numbers)

# Numero más grande

numbers = [15, 65, 59, 50, 26]

number_grand = numbers[0]

for number in numbers:
    if number > number_grand:
        number_grand = number

print("El numero más grande es: ", number_grand)

# Numero pares:

numbers = [15, 65, 59, 50, 26]

number_par = []

for number in numbers:
    if number % 2 == 0:
        number_par.append(number)

print("los numeros pares son: ", number_par)


# Combinar listas y borderland:

list_one = [21, 2, 65, 99]
list_two = [1, 15, 17, 3]

list_total = list_one + list_two
print("Listas combinadas son: ", sorted(list_total))

# Lista de palabras más largas
list_palabras = ['Sergio', 'Andres', 'Vargasmurcia', 'Alexander']

longe_palabras = ""

for palabra in list_palabras:
    if len(palabra) > len(longe_palabras):
        longe_palabras = palabra

print("Palabra más larga: ", longe_palabras)


# lista

balones = [('Golty', 5000), ('mercure', 6000), ('Nike', 8000), ('Adidas', 7500), ('Nike', 8000)]
total_price_balones = 0

for balon in balones:
    total_price_balones += balon[1]

print(len(balones), balones, total_price_balones)

for balon in balones:
    balon == balones