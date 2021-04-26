n=int(input("Enter the number for which you want to find factorial \n"))
def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)
if n<0:
    print("Factorial of negative number is not possible")
else:
    print("The factorial of ",n,"is : ->",fact(n))