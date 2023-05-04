def perfect(a):
    s=0
    for i in range (1,a):
        if(a%i==0):
            s+=i
    print(s)
    if(s==a):
        return 0
    else:
        return 1
a=int(input("Enter a Number"))
if(perfect(a)):
    print("Not Perfect")
else:
    print("Perfect")

