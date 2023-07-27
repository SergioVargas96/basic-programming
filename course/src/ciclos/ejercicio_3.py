# Imprimir las tablas de multiplicar desde el 1 hasta el 10.

def multiplication_table(init, end):
    for i in range(init, end + 1):
        print(f"Tabla de multiplicar del {i}:")
        for j in range(1, 11):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")

multiplication_table(1,2)