def calculate_discount(price):
    if price > 200:
        discount = price * 0.2
        total = price - discount
        print("Su descuento es: $", discount, "y el total es: ", total)
        return discount, total
    else:
        print("El total a pagar es: $", price)
        return price


