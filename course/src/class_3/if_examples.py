edad = int(input("DIGITE SU EDAD :"))

if edad >= 18:
    print(edad , "tienes la edad para entrar al billar")

else:
    print("No tiene la edad para ingresar")


if edad < 18:
    print("eres menor")
    exit(1)

print("si puede jugar : ")

#Negación: 
if not edad < 18:
    print("eres menor")
    exit(1)
print("si puede jugar : ")

#Bloques alternativos:

num = int(input("DIGITE UN NUMERO :"))

if num > 0 :
    print("Numero positivo")

elif num < 0:
    print("numero negativo")

else:
    print("tu numero es 0") 

# Negacion 

num = int(input("DIGITE UN NUMERO :"))

if num > 0 :
    print("Numero positivo")

elif num < 0:
    print("numero negativo")

else:
    print("tu numero es 0")