# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:29:43 2021

@author: Gobinda
"""

"""
queue is a linear data structure that stores items in First In First Out (FIFO) manner.

Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
Dequeue: Removes an item from the queue.If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
Front: Get the front item from queue – Time Complexity : O(1)
Rear: Get the last item from queue – Time Complexity : O(1)

Implementation-

list
collections.deque
queue.Queue
Stack-

Stack is a linear data structure which follows a particular order in which the operations are performed.
The order may be LIFO(Last In First Out) or FILO(First In Last Out)

empty() – Returns whether the stack is empty – Time Complexity : O(1)
size() – Returns the size of the stack – Time Complexity : O(1)
top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
pop() – Deletes the top most element of the stack – Time Complexity : O(1)
#GeeksforGeeks#
"""
import sys

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
    def popCharacter(self):
        return self.stack.pop()
    def pushCharacter(self, char):
        self.stack.append(char)
    def dequeueCharacter(self):
        char = self.queue[0]
        self.queue = self.queue[1:]
        return char 
    def enqueueCharacter(self, char):
        self.queue.append(char)


s=input("enter the string:")
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    