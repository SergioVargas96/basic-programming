Nombre = input( "DIGITE SU NOMBRE :")
print("Hola " + Nombre.title()) # primera letra de cada palabra en mayuscula
print("Hola " + Nombre.capitalize()) # primera leta de la primera palabra en mayuscula
print("Hola " + Nombre.casefold()) # devuelve una cadena donde todos los caracteres están en minúsculas.
print("Hola " + Nombre.lower()) #todas las letras en minuscula
print("Hola " + Nombre.upper()) # toda la cadena en Mayuscula
t = ("sergio", "andres", "vargas")
print("-".join(t)) # separa las palabras de una tupla por el caracter que se le indique.
print(Nombre.replace("sergio", "Messi")) # reemplaza palabras especificas por las indicadas dentro del metodo. 
print(Nombre.split("s")) # separa las palabras por el caracter indicado y las devuelve en una lista 
