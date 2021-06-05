
num1, operator, num2 = input("Calculate(use space between): ").split()


if operator == "+":
    print(float(num1) + float(num2))
elif operator == "-":
    print(float(num1) - float(num2))
elif operator == "*":
    print(float(num1) * float(num2))
elif operator == "/":
    print(float(num1) / float(num2))
elif operator == "^":
    print(pow(float(num1), float(num2)))
else:
    print("error")
