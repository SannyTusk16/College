def bon(s,g):
    if(g=="m"):
        if(s<10):
            return (s*0.07)
        else:
            return (s*0.05)
    else:
        return (s*0.1)
s=int(input("Enter your Salary"))
g=input("M for Male \nF for Female ")
print("Salary= ",s,"Bonus= ",bon(s,g))
