def ltck(l,s):
    for i in s:
        if i==l:
            return True
    return False
s=input("Enter  string m8")
l=input("Enter a letter m8")
if(ltck(l,s)):
    print("Yes Yes Yes")
else:
    print("No No No")
