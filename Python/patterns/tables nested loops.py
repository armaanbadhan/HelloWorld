n = 1
inner_counter = 0
outer_counter = 0

while n <= 20:
    outer_counter += 1
    i = 1
    while i <= 10:
        print(n, "x", i, "=", n*i)
        i += 1
        inner_counter += 1
    print("\r")
    n += 1

print(inner_counter)
print(outer_counter)
