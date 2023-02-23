name = input( "DIGITE SU NOMBRE :")

if len(name) == 0:
    print("Hola Invitado")
elif name.isalpha():
    print("Hola" , name.lower())
else:
    print("No se permiten Numeros")
