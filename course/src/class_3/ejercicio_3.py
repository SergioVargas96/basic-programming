num_1 = int(input("Digite el primero numero :"))
num_2 = int(input("Digite el segundo numero :"))
num_3 = int(input("Digite el tercer numero :"))

if num_1 == num_2 and num_2 == num_3:
    print("Los numero son iguales")

elif num_1 > num_2 and num_1 > num_3 and num_3 < num_2:
    print(num_1, "Es el numero mayor ", num_3 , "es el numero menor")
elif num_1 > num_2 and num_1 > num_3 and num_2 < num_3:
    print(num_1, "Es el numero mayor ", num_2 , "es el numero menor")

elif num_2 > num_1 and num_2 > num_3 and num_3 < num_1:
    print(num_2, "Es el numero mayor ", num_3 , "es el numero menor")
elif num_2 > num_1 and num_2 > num_3 and num_1 < num_3:
    print(num_2, "Es el numero mayor ", num_1 , "es el numero menor")

elif num_3 > num_1 and num_3 > num_2 and num_1 < num_2:
    print(num_3, "Es el numero mayor ", num_1 , "es el numero menor")
elif num_3 > num_1 and num_3 > num_2 and num_2 < num_1:
    print(num_3, "Es el numero mayor ", num_2 , "es el numero menor")