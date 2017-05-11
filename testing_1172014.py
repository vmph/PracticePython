# -*- coding: utf-8 -*-
"""
Created on Fri Nov 07 14:06:37 2014

@author: Anthony
"""

def removeDups(L1, L2):
    for e1 in L1[:]:
        print e1, L1
        if e1 in L2[:]:
            print e1, L1
            L1.remove(e1)
            
            
L1= [1,2,3,4]
L2= [1,2,5,6]
removeDups(L1,L2)
print "L1=", L1

L= [x**2 for x in range(2,5)]
print "L=", L

mixed = [1, 2, "a", 3, 4.0]
print "mixed=", mixed
D = [x**2 for x in mixed if type(x) == int]
print "D=", D

print type(D)

LL = [1,2,3,4,5,6,7,8,9,10]
print "LL=", LL
evenLL =[]
for e in LL:
    if e%2 == 0:
        print e
        evenLL.append(e)
        
print "evenLL=", evenLL
print ""

monthnum = {'JAN':1, 'FEB':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb', 3:'Mar', 4: 'Apr', 5:'May'}
print "monthnum=", monthnum
print "monthnum is a dictionany and prints out unordered!!!"
keyslist=[]
valueslist=[]
testlist =[]
for e in monthnum:
    # for each key in the dictionary (iterate over keys)
    print "key=",e, "value=", monthnum[e]
    # print out the key and the corresponding value
    testlist.append(e)
    keyslist.append(e)
    # append the key in a list called keys[]
    valueslist.append(monthnum[e])
    # append the values in a list called value[]
keyslist.sort()
testlist.sort()
print "keyslist=", keyslist
print "valueslist=", valueslist
print monthnum.keys()
print testlist
print ""

x=6
print range(2,x-1)
print ""

list3 = [1,2,3,2]
print "list3=", list3
if  all ([i!=0 for i in list3]):
    print "yeah! list3 has all non zeros"

print ""

list1=[4,5,6,7,8,9, 10]
##list2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print list1
list2 = []
for x in list1:
    print ""
    print "x in list1 =", x
    for y in range(2, x):
        print "y=", y
        mod = x % y
        print "mod=", mod
        if mod == 0:
            print x, " is divisible by", y
            print "This is it!", x, "is not a Prime Number"
            break
        else:
            print x, "is not divisible by", y        
            list2.append(mod)            
            print "list2=", list2
        
#                if all ([i!=0 for i in list2]):
#                    print x, "IS A PRIME NUMBER!!!!!!!!!!!!!"




    
    
    