
numbers = [1, 3, 5, 8, 86, 98]
books = ["maths", "maths", "physics", "chemistry", "history", "civics", "PE", "english"]

numbers.extend(books)
numbers.append(707)     # adds at end
numbers.insert(2, "insert")         # inserts at (index, object to be added)
numbers.remove(98)

print(numbers)

numbers2 = [3, 5, 7, 456, 356, 3987]
numbers2.clear()

print(numbers2)

books.pop()        # removes last
print(books.index("history"))  # index of certain element
print(books.count("maths"))   # counts no of time appearing
print(books)

books.reverse()
print(books)

books.sort()
print(books)

books2 = books.copy()
print(books2)
