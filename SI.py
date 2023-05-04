def SI(p,t,r=10):
    return (p*t*r)/100
p=int(input("P= "))
t=int(input("t= "))
a=input("Enter S if the customer is a senior")
if(a=="s"):
    print("SI= ",SI(p,t,12))
else:
    print("SI= ",SI(p,t))
