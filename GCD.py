global c
c=0
def GCD(a,b):
    global c
    c+=1
    if(a%b==0):
        return b;
    else:
        return GCD(b,a%b);
a=int(input("a= "))
b=int(input("b= "))
print("GCD(",a,",",b,") = ",GCD(a,b))
print("The recursion reccured ",c,"times")
