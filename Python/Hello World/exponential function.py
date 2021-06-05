
print(2**3)
print(pow(2, 3))


def raise_to_power(num1, num2):
    result = 1
    for index in range(num2):
        result = result * num1
    return result


print(raise_to_power(2, 3))
