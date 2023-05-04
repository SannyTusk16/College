def paln(s):
    for i in range(0,len(s)):
        if(s[i]!=s[len(s)-i-1]):
            return False
    return True
s=input("Enter a string")
if paln(s):
    print("The Gods Have Spoken The Prophecy")
else:
    print("o.o")
