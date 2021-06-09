class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)

_ = input("enter the number of element:")
a = [int(e) for e in input("array element:").split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)