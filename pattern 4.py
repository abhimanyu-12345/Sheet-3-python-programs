pattern = ""
number = 1
for i in range(5):
    if i % 2 == 0:
        pattern += str(number)
        number += 2 
    else:
        pattern += "*"
    print(pattern)

