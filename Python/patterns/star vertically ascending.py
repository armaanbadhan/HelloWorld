def foo(n):
    for i in range(0, n):
        for _ in range(0, i+1):
            print("*", end="")
        print('\r')


foo(5)
