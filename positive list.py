#Python program to print all positive numbers

number = input("right your list ")
number = number.split()

for x in number:
    y = int(x, base=10)
    if y > 0:
        print(x, end=" ")
    del y
