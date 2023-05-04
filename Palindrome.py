def pal(a):
    n=a
    t=a
    N=0
    q=0
    while(a>0):
        N=N+1
        a=a//10
    print(N)
    for i in range(N):
        r=n%10
        n=n//10
        s=t//10**(N-1-i)
        t=t-(s*(10**(N-i-1)))
        print("r= ",r)
        print("s=",s)
        if(r!=s):
            q=q+1
    if(q==0):
        print("Palindrome")
    else:
        print("Not Palindrome")
a=int(input("Enter a number"))
pal(a)
