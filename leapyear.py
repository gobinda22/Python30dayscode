num=int(input("enter the year "))

if(num%4==0):
    if(num%100==0):
        if(num%400==0):

            print("the year is a leap year")

        else:

             print("the year is not a leap year")
    else:

        print("the year is leap year")

else:

    print("the year is not a leap year")