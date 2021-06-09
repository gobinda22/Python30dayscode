class Person:
    #self is not a keyword its a object we
    # we use it to initialize the value
    def __init__(self,fname ,lname ,id ):
        self.firstname = fname
        self.lastname = lname
        self.idnumber = id
    def display(self):
        print("Name:",self.firstname +" ",self.lastname)
        print("ID:",self.idnumber)
class Student(Person):
    def __init__(self,fname ,lname ,id ,testscore):
        #method to inherit from the Person class
        Person.__init__(self,fname ,lname ,id )
        self.testscore = testscore
    def calculate(self):
        total = 0
        for testscore in self.testscore:
            total = total + testscore

        avg = total / len(self.testscore)

        if 90 <= avg <= 100:
           return 'O'
        if 80 <= avg < 90:
           return 'E'
        if 70 <= avg < 80:
           return 'A'
        if 55 <= avg < 70:
          return 'P'
        if 40 <= avg < 55:
          return 'D'
        return 'T'

line = input("line:").split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
#take as user input
numScores = int(input("total number:"))
scores = list(map(int, input("the scores:").split()))
s = Student(firstName,lastName,idNum ,scores)
#call the display function
s.display()
print("Grade:",s.calculate())





