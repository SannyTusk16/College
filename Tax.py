def tax(a):
    if(a<=1.5):
        return 0
    elif(a<=3):
        return 10
    elif(a<=5):
        return 20
    else:
        return 30
a=int(input("ENTER YOUR TAXABLE INCOME IN LAKHS"))
print("YOUR TAX IS ", tax(a))
