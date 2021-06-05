
haha = ["Armaan", 2, False]
print(haha)

lucky_numbers = [1, 2, 6, 234, 54, 89]
books = ["maths", "physics", "chemistry", "english", "civics", "history"]
#          0          1            2           3         4         5     (index)
#         -6         -5           -4          -3        -2        -1  (index)(negative)
print(books[0])
print(books[-3])
print(books[2])
print(books[1:])        # every element after 1(inc 1)
print(books[-2:])
print(books[2:5])      # 2 to 4 (doesnt include 5th)
print(books[-5:-3])

books[3] = "biology"
print(books[3])

books.append(haha)
print(books)
