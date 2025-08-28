rows = 5
for i in range(1, rows + 1):
    underscores = "_ " * (rows - i)
    stars = "* " * i
    print(underscores + stars)
