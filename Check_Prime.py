n=int(input("Enter the number\n"))
def prime(n):
    po=int(n**0.5)
    if(n<0):
        print("Enter a positive number.")
    elif(n==0 or n==1):
        print("Neither prime nor composite.")
    else:
        for i in range(2,po+1):
            if n%i==0:
                return False;
    return True

print(prime(n))
