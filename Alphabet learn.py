# Given Word
word = "Mississippi"
 
# Take an empty dictionary
dic = {}
 
# loop through every letters of word
for alpha in word:
     
    # check for letter is already
    # present in a dic or not
     
    # if present then increment count by 1
    if alpha in dic:
        dic[alpha] += 1
     
    # otherwise assign 1 to it
    else:
        dic[alpha] = 1
 
print("Given Word:", word)
print("Count of each letters is:")
 
# print letter and its count together
for alpha, count in dic.items() :
    print(alpha,"->",count)
