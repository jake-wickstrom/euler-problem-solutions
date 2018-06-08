# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 12:15:52 2017

@author: jtwic
"""
                
if __name__ == "__main__":
    dimensions = 1001
    # this is the sum of all the squares which have 4 corners. 
    # the expression comes from the fact that the top right corner
    # has a value of the dimension of that square to the power of two.
    # the other 3 values are equal to that square minus the side length,
    # two times the side length and 3 times the side length respectively
    squareSum = sum(16*n**2 - 28*n + 16 for n in range(2,int((dimensions+1)/2 + 1)))
    
    print(squareSum + 1)
                
    