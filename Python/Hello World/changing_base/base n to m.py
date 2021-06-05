def to_decimal(number, base):
    number = str(number)
    decimal = 0
    index = 0
    for i in number[::-1]:
        decimal += (base**index) * int(i)
        index += 1
    return decimal


def to_base(number, base):
    in_base = str()
    base_digits = []
    [base_digits.append(i) for i in range(base)]

    while number not in base_digits:
        in_base += str(number % base)
        number = number//base

    in_base += str(number)
    return int(in_base[::-1])


def base_n_to_m(number, n, m):
    return to_base(to_decimal(number, n), m)


print(to_base(19, 2))
print(base_n_to_m(201, 3, 2))
