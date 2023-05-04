def stuff(s):
    a="aeiouAEIOU?"
    for i in a:
        if(i==s):
            return True
    return False
def count(s):
    c=0
    for i in s:
        if(stuff(i)==True):
            c+=1
    return c
s=input("Enter a string")
print("The Number Of Vowels and Question Marks Is",count(s))
