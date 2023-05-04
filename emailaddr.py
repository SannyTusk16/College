def adrpdr(s):
    st=""
    q=100
    for i in range(len(s)-1):
        if(s[i]=="@"):
            q=i
        if(i>q):
            st+=s[i]
    print(st[:-3:])
s=input("Enter an email address")
adrpdr(s)
