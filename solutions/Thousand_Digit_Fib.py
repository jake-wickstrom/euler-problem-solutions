# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 13:08:54 2017

@author: jtwic
"""

def countDigits(num):
    return len(str(num))

#this exceeds the recursion depth
def fibFinder(digits,num1=1,num2=1,index = 2):    
    a = num1
    b = num2
    if(countDigits(b) == digits):
        return (a,b,index)
    else:
        return fibFinder(digits,b,a+b,index+1)

def nextFib(a,b):
    return a+b;

a = 1;
b = 1;
index = 2;
while countDigits(b) < 1000:
    index += 1
    fib = nextFib(a,b)
    a = b
    b = fib
    
print(index)
