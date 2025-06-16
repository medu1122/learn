
# #This problem was asked by Amazon. 

# Given a string s and an integer k, 
# break up the string into multiple lines such that each line has a length of k or less.
#  You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words.
#   If there's no way to break the text up, then return null.

# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, 
# you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. 
# No string in the list has a length of more than 10.

def checkcharK(string,k):
    if len(string) > k :
        return True
    return False

def breakString(string,k):
    words=string.split()
    z=0
    for i in range(len(string.split())):
        if checkcharK(words[i],k):
            z+=1
            break;
    if (z==0):
        for i in range(len(string.split())):
            print(words[i]+"\n")
    else:
        print("NONE")
string=input("string :")
k=int(input("K :"))
breakString(string,k)
