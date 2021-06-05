def bi_to_dec(n):
    n = n[::-1]
    decimal = 0
    pos = 0
    for i in n:
        i = int(i)
        decimal += i*(2**pos)
        pos += 1
    return decimal


print(bi_to_dec(str(1101010)))
