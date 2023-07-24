price = int(input("DIGITE EL VALOR DEL PRODUCTO: "))
discount = price * 0.2
total = price - discount

if price > 200:
    print("Su descuento es: $", discount)
    print("El total a pagar es: $", total)
else:
    print("el total a pagar es: $", price )