def maxii(*num):
    maxi=0
    for i in num:
        if(i>maxi):
            maxi=i
    return maxi
s=int(input())
t=int(input())
a=int(input())
r=int(input())
p=int(input())
l=int(input())
print("Max of the given list of numbers is ",maxii(s,t,a,r,p,l))
