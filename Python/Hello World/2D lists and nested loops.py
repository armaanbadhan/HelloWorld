
number_grid = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    [0]
]

print(number_grid[0][0])
print(number_grid[2][1])             # [row][column]
print(number_grid[1][2])

for x in number_grid:
    for y in x:
        print(y)
