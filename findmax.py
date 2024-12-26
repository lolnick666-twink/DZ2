def method():
    with open("numbers.txt") as file: list=[int(i) for i in file]
    print("Максимальное число:", max(list+[0])); file.close()
file=open("numbers.txt", "w+")
while True:
    try: a=int(input()); file.write(str(a))
    except: break
file.close(); method()
