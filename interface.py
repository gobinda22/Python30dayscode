class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError
class Calculator(AdvancedArithmetic):#interface class
    def divisorSum(self, n):
        sum = 0
        for i in range(1, n + 1):
            if n % i == 0:
                sum = sum + i
        return sum
        pass


n = int(input("enter the number :"))
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)