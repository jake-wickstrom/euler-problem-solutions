# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 14:09:15 2017

@author: jtwic
"""

#See http://mathworld.wolfram.com/DecimalExpansion.html for a more in depth look
#at the number theory behind the solution

#The following equation is satisfied by a repeating sequence
#for a fraction 1/n.

# 10**s %n = 10**(s+t) %n
#
# where s is the index of the first term of the first repeating sequence
# and t is the length of the repeating sequence

# imagine we are doing long division. If we were to get some integer as a remainder,
# then later in the process that same remainder were to appear, we would have an infinite sequence. 
# This equation has a similar logic. It says that if we increase the number of decimal places available 
# (multiply by factor of 10) and divide by the denominator, if the same remainder appears twice, it will
# appear infinite times and result in a recurring sequence

# note that there are infinite s and t which satisfy this equation for a repeating
# sequence, since the modulus equation will form it's own recurring sequence

# t will evaluate to 1 for non-repeating decimals, rather than 0, but this is fine as we know the largest number of repeating will be more than 1

# all I need to do is find t for all n < 1000 and take the highest one

repeating_lengths = []
for n in range(2,1000):
    exponent = 0
    index = 0
    resultTracker = []
    
    while(True):
        testResult = 10**exponent % n
        if testResult in resultTracker:
            # t = (s+t) - s
            # s+t is the index of the second occurence
            # s is the index of the first occurence
            repeating_lengths.append((index - resultTracker.index(testResult),n))
            break
        resultTracker.append(testResult)
        exponent += 1
        index += 1  
              
print(max(repeating_lengths))