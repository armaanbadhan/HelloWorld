
pos = int()
neg = int()

while True:
    try:
        pos = int(input("No of positive reviews: "))
        neg = int(input("No of negative reviews: "))
        break
    except ValueError:
        print("NOT VALID")

pos_rating = round(pos/(pos + neg), 4)

print("People who like it = " + str(pos_rating * 100) + "%")
