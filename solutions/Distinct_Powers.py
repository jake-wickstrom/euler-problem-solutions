# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 08:58:17 2018

@author: jtwic
"""

primes = [2]

for num in range(3,101):
    #check if the current number is divisible by any of the aleady found primes
    if sum([num%prime == 0 for prime in primes]) == 0:
        primes.append(num)
        
combos = []

for a in range(2,101):
    #find prime factorization of a, then multiply by b
    num = a
    index = 0
    combo = [0 for i in range(len(primes))]
    
    while not num == 1:
        if num % primes[index] == 0:
            combo[index] = combo[index] + 1
            num = num/primes[index]
        else:
            index = index + 1
    #iteratively reduce the given base number into its prime factorization by pulling out prime factors one by one
    #start with smallest prime and continue to pull out primes until the full prime factorization is complete
    
    for b in range(2,101):

        #multiply factorization by power which base is raised to        
        pow_combo = [item*b for item in combo]
        #if the combo just calculated is unique
        if sum(pow_combo == existing_combo for existing_combo in combos) == 0:
            combos.append(pow_combo)
    
print(len(combos))
                
            
    