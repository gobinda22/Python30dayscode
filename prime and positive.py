def prime(n):

 if(n>1):

    for i in range(2,n):

      if(n%i==0):

        print("the number is not prime")
        break
    else:

        print("the number is prime")
        break
num=int(input("enter the number"))

if(num>0):

        prime(num)

else:

        print("enter a positive number")
