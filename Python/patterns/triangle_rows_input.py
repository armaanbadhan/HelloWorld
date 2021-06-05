def foo(n):
    for i in range(n):
        for k in range(1, n-i):
            print(" ", end="")
        for j in range(2*i + 1):
            print("*", end="")
        print("\r")


def foo1(n):
    i = 0
    while i <= n:
        star = 1
        space = 1
        while space <= n-i:
            print(" ", end="")
            space += 1
        while star <= 2*i + 1:
            print("*", end="")
            star += 1
        print("\r")
        i += 1


def foo2(n):
    for i in range(n):
        print((n-i-1) * " ", end='')
        print(((2*i) + 1) * "*")


foo2(5)
