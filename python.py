def function_1():
    x = 5
    y = 10
    return x


def function_2():
    z = 5
    w = 20
    return z


def nueva_function():
    resultado_function_1 = function_1()
    resultado_function_2 = function_2()
    variable_x_resultado_function_1 = resultado_function_1
    variable_z_resultado_function_2 = resultado_function_2

    if variable_x_resultado_function_1 == variable_z_resultado_function_2:
        print("Las variables son iguales")
    else:
        print("No son iguales ")


nueva_function()
