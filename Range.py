def rang(a,b):
    for i in range(a,b+1):
        if(a==i):
            return 0
    return 1;
a=int(input("Enter the range "))
b=int(input())
c=int(input("Enter a Number "))
if (rang(a,b)==0):
    print("IN RANGE")
else:
    print("NOT IN RANGE")
