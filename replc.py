def replc(l,r,s):
    st=""
    for i in range(len(s)):
        if s[i:len(l)]==l:
            st+=r
        else:
            st+=s[i]
    print(st)
s=input("Enter a string")
l=input("Enter the charcter to be replaced")
r=input("Enter the replacement character")
replc(l,r,s)
