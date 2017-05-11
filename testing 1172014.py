# -*- coding: utf-8 -*-
"""
Created on Fri Nov 07 14:02:17 2014

@author: Anthony
"""

def removeDups(L1, L2):
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)
            
            
L1= [1,2,3,4]
L2= [1,2,5,6]
removeDups(L1,L2)
print "L1=", L1
