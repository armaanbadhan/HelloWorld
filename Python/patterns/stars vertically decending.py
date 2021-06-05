def foo(n):
    for i in range(n):
        i += 1
        for _ in range(0, n-i+1):
            print("*", end="")
        print("\r")


foo(5)
