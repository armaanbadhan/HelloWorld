def to_base(x, base):
    in_binary = str()
    base_digits = []
    [base_digits.append(i) for i in range(base)]
    print(base_digits)

    while x not in base_digits:
        print(x)
        in_binary += str(x % base)
        x = x//base

    print(x)
    in_binary += str(x)
    return in_binary[::-1]


print(to_base(20, 3))
