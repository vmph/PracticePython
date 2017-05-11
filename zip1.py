# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 12:59:55 2014

@author: Valerie
"""

  
#n0 = 5
#n = 15
#j = 0
#for i in range(n0,n+1):
#    print ""
#    print"increment i goes to:", i
#    if  (i % 3 == 0 and i % 5 == 0):
#        j = j + 15
#        print "j must add +15: j =", j
#    elif (i % 3 == 0):
#        j = j + 3
#        print "j must add +3: j =", j
#    elif (i % 5 == 0):
#        j = j + 5
#        print "j must add +5: j =", j
#    else:
#        j = j + 1
#        print "j must add +1: j =", j      
 
    
  
n0 = 5
n = 15
count = 0
for i in range(n0,n+1):
    if  (i % 3 == 0 and i % 5 == 0):
        count += 15
    elif (i % 3 == 0):
        count += 3
    elif (i % 5 == 0):
        count += 5
    else:
        count += 1
print count
##################################################################

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)
        
        
def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n
   else:
      return n * f(n-1)
        
