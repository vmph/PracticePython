# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:43:25 2015

@author: Valerie
"""
# Ans:
def f(n):
    for x in range(n):
        yield x**3    
  
for x in f(5): # what should the function f be ? (see above ans)
    print x
    
############################################    
# build a string with the numbers from 0 to 100
def build(n):
    L =[]  # define empty list
    for x in range(n):
        L.append(x)  # append each integer inside the list L
#        print L
    print "".join(str(i) for i in L) # for each int of L, transform into a str and join
#############################################      
# OR
"".join(str(x) for x in xrange(101))        
#########################################################
# Reading and printing content of file using exceptions
try:
    with open("output.txt", 'r') as f:
        print f.read()
except IOError:
    print "No such file exist"
########################################################
# difference between range() and xrange()
a = sum(range(1,101))
b = sum(xrange(1,101))
    
################################################
# List comprehension
[ x ** 3 for x in range(5)]
#######################################################
#Make a list with unique element from a list with duplicate elemetns
# Use the set() function
dup_list = [1,2,3,4,4,4,5,1,2,7,8,8,10]
unique_list = list(set(dup_list))
print unique_list
######################################################
# map a list to another list
items = [1, 2, 3, 4, 5]

squared = []
for x in items: 
    squared.append(x ** 2)

squared
# Using the built-in map(afunction, asequence)
def sqr(x):
    return x**2
    
list(map(sqr, items))

list(map((lambda x: x **2), items))  # using lambda function
####################################################
# Given a list of N numbers, use a list comprehension to produce a new list 
# only containing even numbers from elements that have even indicies
L=[1,6,4,3,5,8,3,8,6,9,3]
L=[0,1,2,3,4,5,6,7,8,9,10]
def checking(L):
    i=0
    L1=[]
    for i in range(len(L)):
        if i%2 == 0 and L[i]%2 == 0:
            print "index and element are even", i, L[i]
            L1.append(L[i])
    return L1        
# now with a list comprehension
[x for x in list[::2] if x%2 == 0]
######################################################
def extendList(val, list=[]):
    list.append(val)    # beware that new default list is created only once when the function is defined
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a') 

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3    

############ Note the difference: 
def extendList1(val, list=None):
    if list is None: # always begin a new list when no list argumnet is specified
        list=[]
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3 
########################################################
# Write a function, tokenize_string(input_string, delimiter_list) 
#that returns a list of strings that are separated by the delimiters.
# SSS = "How now, Mrs. Brown Cow"  must return ['How', 'now', 'Mrs', 'Brown', 'Cow']
def tokenize_string(input_string, delimiter_list):
    import re
    delimiter_list = ','
    L = re.split(delimiter_list, input_string)
    return L
    
    
    
    
###################################################        
#Write a string to find a substring in a given string. Do this in O(n) or better

#Write a function to implement strstr() i.e. find the first occurrence of one string inside another string.

#Write a program to print out a multiplication table, from 1x1 to 12x12. This should look like:

#