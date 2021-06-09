from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
        #abstract method call
    @abstractmethod
    def display(): pass
class MyBook(Book):
    def __init__(self,title,author,price):
        Book.__init__(self,title,author)
        self.price =price
        #we can inherit and modify the display class as our wish it is main point of abstract class
        #we can modify it multiple time
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)


title=input("enter the title:")
author=input("enter the author name:")
price=int(input("enter the price:"))
new_novel=MyBook(title,author,price)
new_novel.display()