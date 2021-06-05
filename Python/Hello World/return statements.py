
num1, power = input("Enter in format - [number, power] :").split("^")


def cube(num1):
    return str(pow(float(num1), float(power)))
# can't execute anything after the "return" statement



result = cube(num1)
print(num1 + " to the power " + power + " is " + "\"" + result + "\"")
