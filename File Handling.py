file_q = open("Quote.txt","r")
for x in file_q:
    print(x)

file_b = open("Blogging.txt","w")
file_b.write("Hey! Welcome to the Blog of my Experiance to Travel Assam")

file_b = open("Blogging.txt","a")
file_b.writelines(" So, the trip starts from Ajmer, & it was a rainy day")
file_b.writelines(" by crossing the terrifing traffic, around 10 am, I reach the Railway Junction of Ajmer")
file_b = open("Blogging.txt","r")
