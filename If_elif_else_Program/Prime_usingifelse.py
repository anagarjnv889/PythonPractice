n=int(input("Enter the number\n"))
po=int(n**0.5)
num=po+1
flag=True
if(n<0):
    print("Enter a positive number.")
elif n==1 or n==0:
    print("Neither prime nor composite number.")
else:
    for i in range(2,n):
        if n%i==0:
            flag=False
            break
    if flag:
        print(n,"is a prime number.")
    else:
        print(n,"is not a prime number.")