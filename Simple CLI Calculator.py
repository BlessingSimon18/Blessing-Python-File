def add(number1, number2) :
    return number1 + number2
def subtract(number1, number2) :
    return number1 - number2
def multiply(number1, number2) :
    return number1 * number2
def divide(number1, number2) :
    return number1 / number2
def modulus(number1, number2) :
    return number1 % number2
print("Please select operation -\n" \
    "1. Addition\n" \
    "2. Subtraction\n" \
    "3. Multiplication\n" \
    "4. Division\n" \
    "5. Modulus\n")
select = int(input("select operations from 1, 2, 3, 4,5 :"))

number_1 = int(input("enter first number: "))
number_2 = int(input("enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
elif select == 5:
    print(number_1, "%", number_2, "=",
                    modulus(number_1, number_2))
else:
    print("Invalid input")