def sum(*num):
    s=0
    for i in num:
        s=s+i
    return s;
a=input("Enter few Numbers")
print(sum(tuple(a)))
