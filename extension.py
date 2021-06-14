#extension 

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
