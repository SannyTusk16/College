def strw(s):
    c=0
    for i in s:
        if(i==" "):
            c+=1
        elif(i=="."):
            c+=1
    return c
s=input("Enter a string")
print("The Number Of Words In The String",s,"Are",strw(s))
