def calculate_discount_products(amount, price):
    price_total = price * amount
    discount_10 = price_total * 0.10
    discount_5 = price_total * 0.05

    if amount >= 20:
        total = price_total - discount_10
        print("su descuento del 10% es: $", discount_10)
        print("El total a pagar con descuento del 10% es: $", total)
        return discount_10, total

    elif 10 <= amount < 20:
        total = price_total - discount_5
        print("su descuento del 5% es: $", discount_5)
        print("El total a pagar con descuento del 5% es: $", total)
        return discount_5, total
    else:
        discount = 0
        print("El total a pagar sin descuento es: $", price_total)
        return discount, price_total


calculate_discount_products(9, 200)
