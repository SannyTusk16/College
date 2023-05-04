def fact(a):
    if(a==0):
        return 1;
    else:
        return a*(fact(a-1))
n=int(input("n = "))
r=int(input("r = "))
print("(n,r)= ",fact(n)/(fact(n-r)*fact(r)))
