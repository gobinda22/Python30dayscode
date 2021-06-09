# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 12:28:42 2021

@author: Gobinda
"""

class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise ValueError('n and p should be non-negative')
        return n ** p
myCalculator=Calculator()
T=int(input("enter the test case:"))
for i in range(T):
    n,p = map(int, input("enter the numbers:").split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
