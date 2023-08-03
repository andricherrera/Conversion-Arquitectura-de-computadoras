def decimal_to_base(number, base):
    # Función para convertir un número decimal a otra base
    digits = "0123456789ABCDEF"
    result = ""
    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number = number // base
    return result

def base_to_decimal(number, base):
    # Función para convertir un número de otra base a decimal
    digits = "0123456789ABCDEF"
    result = 0
    power = 0
    for digit in reversed(number):
        result += digits.index(digit) * (base ** power)
        power += 1
    return result

def main():
    print("Convertir un número de una base a otra.")
    try:
        number = input("Ingrese el número: ")
        current_base = int(input("Ingrese la base actual del número (2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16): "))
        new_base = int(input("Ingrese la base a la que desea convertirlo (2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16): "))

        if current_base not in [2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16] or new_base not in [2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16]:
            print("Las bases deben ser 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15 o 16.")
        else:
            if current_base == 10:
                number_decimal = int(number)
            else:
                number_decimal = base_to_decimal(number, current_base)

            if new_base == 10:
                result = str(number_decimal)
            else:
                result = decimal_to_base(number_decimal, new_base)

            print(f"El número {number} en base {current_base} es {result} en base {new_base}.")

    except ValueError:
        print("Ha ocurrido un error. Asegúrese de ingresar números válidos.")

if __name__ == "__main__":
    main()
