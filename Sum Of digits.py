def digit(a):
    """NO. OF DIGITS?"""
    n=0
    while(a>0):
        n+=1
        a//=10
    print(n)
    return n
def sumi(a):
    """SUM OF ALL DIGITS"""
    s=0
    for i in range(digit(a)):
        s+=(a%10)
        print(s,end="\t")
        a=(a-(a%10))//10
    return s
a=int(input("Enter a number"))
print(sumi(a))
