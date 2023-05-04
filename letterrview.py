def deez(c,s):
    co=0
    for i in range(0,len(s)):
        if(s[i]==c):
            print("Index=",i)
            co+=1
    print("No of occurances ",co)
c=input("Enter a character")
s=input("Enter a string")
deez(c,s)
