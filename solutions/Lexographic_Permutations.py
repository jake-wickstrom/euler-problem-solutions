# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 12:06:03 2017

@author: jtwic
"""

start = "0123456789"

class lexographicPermuter():
    def __init__(self,start):
        self.start_seq = [int(x) for x in str(start)]
        self.current_seq = self.start_seq
    
    def nextPermuation(self):
        sequence = list(range(1,len(self.current_seq)))
        assigned = False
        #find the longest decreasing sequence in the current permutation
        for i in sequence:
            if(self.current_seq[-i] < self.current_seq[-i-1]):
                pass
            else:
                tail = self.current_seq[-i:]
                pivot = self.current_seq[-i-1]
                head  = self.current_seq[:-i-1]
                assigned = True
                break
        
        if(assigned == False):
            print("No further sequences")
            return self.current_seq
        #replace the next element after the decreasing sequence with the smallest number in the decreasing sequence
        #this number must be greater than the element it is replacing
        
        for i in range((len(tail))):               
            if tail[-i-1] > pivot:
                temp = tail[-i-1]
                tail[-i-1] = pivot
                pivot    = temp
                break
        
        #reverse the order of the new tail and return        
        result = []
        result.extend(head)
        result.append(pivot)
        tail.reverse()
        result.extend(tail)
        #result.append(tail.reverse())
        self.current_seq = result
        return self.current_seq

solver = lexographicPermuter(start)
#calculate up to 999 999 permutations (including the starting one)
for i in range(999998):
    solver.nextPermuation()
    
#print the last one
print(solver.nextPermuation())



