print("___________________________________\n")
print("Welcome to Python Calculator")
print("___________________________________\n")


# Arithmetic Calculator functions|||||||||||||||||||||||||||||||||||||||||||||||||||||
# Addition calculation
def addition():
    a = int(input("Enter first number\n"))
    b = int(input("Enter second number\n"))
    print("Sum of", a, "and", b, "is -> ", a + b)
    print("Would you like to continue, then press 1, otherwise press 0")
    n = int(input("Enter your choice 1/0 \n"))
    if n == 1:
        take_input()
    elif n == 0:
        print("Thank you")
    else:
        print("Enter a valid input")


# Subtraction calculation
def subtraction():
    a = int(input("Enter first number\n"))
    b = int(input("Enter second number\n"))
    print("Difference of", a, "and", b, "is -> ", a - b)
    print("Would you like to continue, then press 1, otherwise press 0")
    n = int(input("Enter your choice 1/0 \n"))
    if n == 1:
        take_input()
    elif n == 0:
        print("Thank you")
    else:
        print("Enter a valid input")


# Multiplication calculation
def multiplication():
    a = int(input("Enter first number\n"))
    b = int(input("Enter second number\n"))
    print("Multiplication of", a, "and", b, "is -> ", a * b)
    print("Would you like to continue, then press 1, otherwise press 0")
    n = int(input("Enter your choice 1/0 \n"))
    if n == 1:
        take_input()
    elif n == 0:
        print("Thank you")
    else:
        print("Enter a valid input")


# Division calculation
def division():
    a = int(input("Enter first number\n"))
    b = int(input("Enter second number\n"))
    if b > 0:
        print("Division of", a, "and", b, "is ->", a / b)
        print("Would you like to continue, then press 1, otherwise press 0")
        n = int(input("Enter your choice 1/0 \n"))
        if n == 1:
            take_input()
        elif n == 0:
            print("Thank you")
        else:
            print("Enter a valid input")
    else:
        print("Please enter a valid value of divisor")


# Modulus calculation
def modulus():
    a = int(input("Enter first number\n"))
    b = int(input("Enter second number\n"))
    if b > 0:
        print("Modulus of", a, "and", b, "is ->", a % b)
        print("Would you like to continue, then press 1, otherwise press 0")
        n = int(input("Enter your choice 1/0 \n"))
        if n == 1:
            take_input()
        elif n == 0:
            print("Thank you")
        else:
            print("Enter a valid input")
    else:
        print("Please enter a valid value of divisor")


# Advance Calculator functions|||||||||||||||||||||||||||||||||||||||||||||||||||||
# HCF calculation
def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


# Power calculation
def power():
    a = int(input("Enter the base number\n"))
    b = int(input("Enter the power number\n"))
    print(a, "raise to the power", b, "is ->", a ** b)
    print("Would you like to continue, then press 1, otherwise press 0")
    x = int(input("Enter your choice 1/0 \n"))
    if x == 1:
        take_input()
    elif x == 0:
        print("Thank you")
    else:
        print("Enter a valid input")


# Square root calculation
def square_root():
    a = int(input("Enter the number\n"))
    print("Square root of", a, "is -> ", a ** 0.5)
    x = int(input("Enter your choice 1/0 \n"))
    if x == 1:
        take_input()
    elif x == 0:
        print("Thank you")
    else:
        print("Enter a valid input")


# Factorial calculation
def fact():
    n = int(input("Enter the number for which you want to calculate factorial\n"))
    if n < 0:
        print("Factorial of a negative number can not be calculated. Please enter a positive number.")
    elif n == 0:
        print("Factorial of", n, "is -> ", 1)
    else:
        f = 1
        for i in range(1, n + 1):
            f = f * i
        print("Factorial of", n, "is -> ", f)
    x = int(input("Enter your choice 1/0 \n"))
    if x == 1:
        take_input()
    elif x == 0:
        print("Thank you")
    else:
        print("Enter a valid input")


# Prime check
def prime():
    n = int(input("Enter a number\n"))
    flag = True
    if n < 0:
        print("Enter a positive number.")
    elif n == 1 or n == 0:
        print("Neither prime nor composite number.")
    else:
        for i in range(2, n):
            if n % i == 0:
                flag = False
                break
        if flag:
            print(n, "is a prime number.")
        else:
            print(n, "is not a prime number.")
    x = int(input("Enter your choice 1/0 \n"))
    if x == 1:
        take_input()
    elif x == 0:
        print("Thank you")
    else:
        print("Enter a valid input")


def arithmetic_operation():
    print("____________________________________")
    print("\nWelcome to Arithmetic Calculator")
    print("____________________________________\n")
    print("\nPress 1 for Addition................")
    print("Press 2 for Subtraction.............")
    print("Press 3 for Multiplication..........")
    print("Press 4 for Division................")
    print("Press 5 for Modulus.................\n")
    n = int(input("Enter your choice for Arithmetic Operation\n"))
    if n == 1:
        addition()
    elif n == 2:
        subtraction()
    elif n == 3:
        multiplication()
    elif n == 4:
        division()
    elif n == 5:
        modulus()
    else:
        print("Enter a valid input\n")


def advance_operation():
    print("____________________________________")
    print("\nWelcome to Advance Calculator")
    print("____________________________________\n")
    print("\nPress 1 for HCF/GCD................")
    print("Press 2 for Power of a number........")
    print("Press 3 for Square root of a number..")
    print("Press 4 for Factorial of a number....")
    print("Press 5 to check prime or not......\n")
    n = int(input("Enter your choice for Advance Operation\n"))
    if n == 1:
        a = int(input("Enter first number\n"))
        b = int(input("Enter second number\n"))
        print("HCF of", a, "and", b, "is -> ", hcf(a, b))
    elif n == 2:
        power()
    elif n == 3:
        square_root()
    elif n == 4:
        fact()
    elif n == 5:
        prime()
    else:
        print("Enter a valid input\n")


def take_input():
    print("Press 1 for Arithmetic Operation")
    print("Press 2 for Advance Operation")
    n = int(input("Enter your choice\n"))
    if n == 1:
        arithmetic_operation()
    elif n == 2:
        advance_operation()
    else:
        print("Enter a valid input")


take_input()
