n = int(input(" max stars in a line:"))

for i in range(2*n - 1):
    for j in range(5 - abs(i - 4)):
        print("*", end="")
    print("\r")
