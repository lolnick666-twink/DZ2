with open ("numbers.txt") as file:
    list = [int (i) for i in file]
print("Максимальное число:", max(list))
