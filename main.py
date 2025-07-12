import math
def calculator():
    while True:
        try:
            print("a is the first number and b is the second number")
            a = float(input("Enter the value of a: "))
            O = input("Enter the operation you want to perform from these +, -, *, /, a^b , a^2 , sqr (square root), 1/a: ")

            if O in ["+", "-", "*", "/", "a^b"]:
                b = float(input("Enter the value of b: "))

            print("======")

            match O:
                case "+":
                    print(f"The result will be {a+b}")
                case "-":
                    print(f"The result will be {a-b}")
                case "/":
                    print(f"The result will be {round((a/b),4)}")
                case "*":
                    print(f"The result will be {a*b}")
                case "a^b":
                    print(f"The result will be {pow(a,b)}")
                case "sqr":
                    print(f"The result will be {round(math.sqrt(a),3)}")
                case "1/a":
                    print(f"The result will be {round(1/a,2)}")
                case "a^2":
                    print(f"The result will be {round(pow(a,2))}")
                case _:
                    print("Invalid operator!")
        except ValueError:
            print("Enter only integer/float values of a and b")
        except ZeroDivisionError:
            print("Do not divide by zero!")
        except Exception as e:
            print("Something went wrong:", e)

        use_again = input("Do you want to use calculator again?\n(yes/no): ").lower()
        if use_again != "yes":
            print("Bye!")
            break
        print("======")

calculator()
print("======")
