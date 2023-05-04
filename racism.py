def vow(s):
    a="aeiouAEIOU"
    for i in a:
        if(i==s):
            return True
    return False
def racism(s):
    for i in s:
        if(vow(i)==False):
            print(i,end="")
s=input("Enter a string")
racism(s)
