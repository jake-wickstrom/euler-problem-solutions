# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:14:38 2017

@author: jtwic
"""
from math import sqrt 

a_range = 999
b_range = 1000

longest_prime_seq = 1;
best_a = 1
best_b = 0

def quadratic(a,b,n):
    return n**2 + a*n + b

def isPrime(n):
    fail = False
    
    #negative numbers can not be prime
    if(n < 1):
        return False
    
    for potentialFactor in range(2,int(sqrt(n) + 1)):
        if(n % potentialFactor == 0):      
            fail = True 
    return not fail


for a in range(-a_range,a_range):
    for b in range(-b_range,b_range):
        fail = False
        
        #when n = 0, the quadratic is equal to b. Therefore b must be prime
        if not isPrime(b):
            pass
        
        for i in range(longest_prime_seq):
            testValue = quadratic(a,b,i)
            #preliminary check: if a number is not an integer it is certianly not prime
            if(int(testValue) != testValue):
                fail = True
                break
            
        n = 1            
        if fail is False:
            counter = 0;
            if(isPrime(quadratic(a,b,0))):
                while(isPrime(quadratic(a,b,n))):
                    n += 1
                    
        if(n > longest_prime_seq):
            longest_prime_seq = n
            best_a = a
            best_b = b
                
            
            
print(best_a,best_b, longest_prime_seq)