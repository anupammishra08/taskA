# taskA
#first task is a python program which accepts the radius of a circle and compute it &amp; second is to find which type of file is entered by its extension

#task1
r = float(input("input the radius of the circle: "))

PI = 3.142
area =PI * r * r

print("The area of circle with radius is: ",area)


#task2

file = input("Input the Filename: ")
exten = file.split('.')[1]


if exten == 'py':
    pro = 'python'

elif exten == 'c':
    pro = 'C'
elif exten == 'hh':
   pro = 'C++'
elif exten == 'java':
    pro = 'java'
elif exten == 'js':
    pro = 'javascript'
else :
    pro = "i didn't find something like that"

print("The extension of the file is: " ,pro)
