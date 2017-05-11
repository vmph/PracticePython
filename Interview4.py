# -*- coding: utf-8 -*-
"""
Created on Mon May 04 12:27:05 2015

@author: Valerie
"""

# Wrap the strin grepeated ten times to a max width of 78 chars, starting each line with "> " 
def wrap(string, length):

    while len(string):
        print("> " + string[0:length - 1])
        string = string[length - 1:].strip()


wrap("The quick brown fox jumps over the lazy dog. " * 10, 78)
###################################################################
# yes, Python has way too many forms of string literals :)
print "\\#{'}${\"}/"
print "\\#{'}${"'"'"}/"
print r"""\#{'}${"}/"""
print '\\#{\'}${"}/'
print '\\#{'"'"'}${"}/'
print r'''\#{'}${"}/'''
#############################################################
text = """This
Is
A
Multiline
String"""
# with proper indentation
text = (
		"This\n"
		"Is\n"
		"A\n"
		"Multiline\n"
		"String"
	)
##############################################################
# reverse a string
"reverse me"[::-1]

# reverse the words in a string
' '.join(reversed("This is a end, my only friend!".split()))

# make a string upper
"Space Monkey".upper()

# make a string lower
"Caps ARE overRated".lower()

# capitalize fist letter of each word
from string import capwords
capwords("man OF stEEL")
# OR
' '.join(s.capitalize() for s in "man OF stEEL".split())
"man OF stEEL".title()
##############################################################
import random

random.seed(12345)
list1 = [random.randint(1,10) for x in range(5)]
list1
random.seed(12345)
list2 = [random.randint(1,10) for x in range(5)]
list2
assert(list1==list2)  # what does assert() do ???
##############################################################
# About files in python
contents = open('myFile.txt', 'rt')
contents.read()
# Process a file one line at the time
for no, line in enumerate(open(__file__)):
    print "{0}> {1}".format(no+1, line.rstrip())
    
# Write a string in a file
tt= open('test.txt', 'wt')
tt.write('Hello World!')
# Append to a file
tt= open('test.txt', 'at')
tt.write('Hello World!\n')
###############################################################
# Find all Pythagorean triangles with length or height less than or equal to 20
#Sort your results by the size of the hypotenuse
def pythagorean(num):
    from math import sqrt

    ret = []
    a = 1
    while a <= num:
        b = 1
        while b <= num:
            c = sqrt((a**2)+(b**2)) 
            if int(c) == c and sorted([a,b,int(c)]) not in ret:
                ret.append(sorted([a,b,int(c)]))
            b +=1
        a +=1       
    print ret 
    return ret

#or if you wanna get snarky..

w=sorted(set([tuple(sorted((a,b,int(sqrt((a**2)+(b**2)))))) for a in xrange(1,21) for b in xrange(1,21) if int(sqrt((a**2)+(b**2))) == sqrt((a**2)+(b**2))]))
print w
##############################################################################
#Find the largest positive integer that divides two given numbers without a remainder.
# An recursive way
def gcd_recursive(i, j):
    if min(i, j) == 0:  # base case
        return max(i, j)
    else:               # recursive case 
        print i, j
        return gcd_recursive(min(i, j), abs(i - j))

gcd_recursive(24, 2576)

# an iterative way        
def gcd_iterative(i, j):
    while min(i, j) != 0:
        i, j = min(i, j), abs(i - j)
        print i, j
    return max(i, j)

gcd_iterative(24, 2576)

# Using gcd() from the fractions library    
if __name__ == "__main__":
    print gcd_recursive(8, 12)
    print gcd_iterative(8, 12)
from fractions import gcd
print gcd(8, 12)
#################################################################################
# Given sorted array of 0 and 1, find the numb of O in it. Write recursive and iterative versions.
def findzero1(A):
    count = 0
    for i in range(len(A)):
        if A[i] == 0:
            count += 1
    print "count of zeros = ", count
    return count        
###########################################
A={2,4,3,5,6,8}
B={9,2,7,6}
A & B

    

