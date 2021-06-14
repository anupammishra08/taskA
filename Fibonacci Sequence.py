# Fibonacci Number
how_many = int(input("how many number of time you want Fibonacci Sequence: "))
def fib(n):
    a = 0
    b = 1

    if how_many == 1:
        print(a)
    
    elif how_many < 0:
        print("Invaild value enter a vaild one")

    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)
     


fib(how_many)
