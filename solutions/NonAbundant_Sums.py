# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:18:12 2017

@author: jtwic
"""
from math import sqrt

def factor(num):
    factors = set()
    pairs   = set()
    for n in range(1,int(sqrt(num) + 1)):           
        if(num % n == 0):
            factors.add(n)

    for factor in factors:
        if(factor != sqrt(num)):
            pairs.add(num/factor)
        
    [factors.add(x) for x in pairs]
    
    factors.remove(num)
    
    return factors

def isAbundant(num):
    factors = factor(num)
    if(sum(factors) > num):
        return True
    else:
        return False
        
class abundantChecker():
    def __init__(self):
        self.abundantNumbers = []

        for i in range(1,28123):
            if(isAbundant(i)):
                self.abundantNumbers.append(i)
                
    def twoAbundantSum(self,num):
        relevantAbundants = [x for x in self.abundantNumbers if x<num]
        
        for relevantAbundant in relevantAbundants:
            if num - relevantAbundant in relevantAbundants:
                return True
            
        return False
    
checker = abundantChecker()
solution = 0

for i in range(1,28123):
    print("Checked {} numbers.".format(i), end = "\r")
    if not checker.twoAbundantSum(i):
        solution += i
        
print("Solution is {}".format(solution))


