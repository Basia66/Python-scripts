def addition(number, number2):
    return number + number2


def subtraction(number, number2):
    return number - number2


def multiplication(number, number2):
    return number * number2


def division(number, number2):
    return number / number2


def exponentiation(number, power):
    number2 = number
    for x in range(power-1):
        number2 *= number
    return number2
    # return number ** power


def root(number, power):
    return number ** (1/power)


def main():
    number = int(input("Write a number: "))
    number2 = int(input("Write a number: "))
    print(addition(number, number2))
    print(subtraction(number, number2))
    print(multiplication(number, number2))
    print(division(number, number2))
    print(exponentiation(number, number2))
    print(root(number, number2))


if __name__ == '__main__':
    main()
