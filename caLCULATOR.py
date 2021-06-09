def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mult(a, b):
    return a*b
def div(a, b):
    return a/b

print("enter your choice")
print("1.add")
print("2.sub")
print("3.mult")
print("4.div")

while True:
    choice = input("enter choice(1/2/3/4): ")

    if choice in('1','2','3','4'):

        num1=float(input("enter your first number: "))
        num2=float(input("enter your second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
            print("error 404 occur")

