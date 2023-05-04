def powi(a,n):
    if(n==0):
        return 1
    else:
        return (a*powi(a,n-1))
a=int(input("Base= "))
b=int(input("Power= "))s
print(a,"^",b,"=",powi(a,b))
