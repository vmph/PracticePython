# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:56:26 2015

@author: Valerie
"""

# Find the longest running positive sequence in an array

###################fROM langref.org : exercises for LISTS ##############################
# Join elements of list by comma and space
L=["apple", "banana", "cerise", "pomme"]
S=", ".join(L)
print S    
########################################################################################
# Join  the elements of list in correct English
def join(*x):
    if len(x) <= 2:
        return ' and '.join(x)
    else:
        return ', '.join(x[:-1] + ('and ' + x[-1],))

if __name__ == "__main__":
    assert join("Apple", "Banana", "Carrot") == "Apple, Banana, and Carrot"
    assert join("One", "Two") == "One and Two"
    assert join("Lonely") == "Lonely"
    assert join(*[]) == ""    
#######################################################################################
# Produce the combination of 2 lists
#Given two lists, produce the list of tuples formed by taking the combinations from the individual lists. 
# E.g. given ["a", "b", "c"] and [4, 5], produce the list: [["a", 4], ["b", 4], ["c", 4], ["a", 5], ["b", 5], ["c", 5]] 
    
[(x, y) for y in [1,2] for x in ['a','b','c']]
# OR
import itertools
[x for x in itertools.product(["a", "b", "c"], [4, 5])]
########################################################################################
# From a list showing the duplicate entries of a list
import itertools
input = ["andrew", "bob", "chris", "bob"] 
input.sort()
output = [k for k, g in itertools.groupby(input, lambda x: x) if len(list(g)) > 1]
#########################################################################################
# Fetch an element of a list by index
list = ['One', 'Two', 'Three', 'Four', 'Five']
list[2]
########################################################################
# Fetch the last element of a list
list = ['Red', 'Green', 'Blue']
list[-1]
########################################################################
# Find the common items in two lists
beans = ['broad', 'mung', 'black', 'red', 'white']
colors = ['black', 'red', 'blue', 'green']
set(beans)
set(colors)

common = [x for x in beans if x in colors]
# OR
common = set(beans) & set(colors)
########################################################################
# Display the unique items in a list
ages = [18, 16, 17, 18, 16, 19, 14, 17, 19, 18]

unique_ages = list(set(ages))
#######################################################################
# More on set() : Sets are lists with no duplicate entries.
txt = "my name is Eric and Eric is my name"
t = txt.split()  # create a list with items from txt
a = set(t)   # makes it unique
print (a) 
print set("my name is Eric and Eric is my name".split())
# Can do mathematical operations on sets
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

a.intersection(b)
b.intersection(a)
a & b

a.symmetric_difference(b)
b.symmetric_difference(a)
a ^ b

a.difference(b)
a - b
b.difference(a)
b - a
a.union(b)
a | b
#################################################################################
# Generators
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in xrange(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
    print "And the next number is... %d!" % random_number
################################################################################
# List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))


sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]

################################################################################

############################################################
# Remove an element from a list by index
myList = ['Apple', 'Banana', 'Carrot']
print myList
del myList[0]
# or
myList.pop(0) # returns 'Apple'
print myList
########################################################################
# Remove the last element of a list
myList = ['Apple', 'Banana', 'Carrot']
myList.pop()
########################################################################
# Rotate a list by removing the first item and placing it on the end
l = ["apple", "orange", "grapes", "bananas"]
first, l = l[0], l[1:] + l[:1]
fruit = ['apple', 'orange', 'grapes', 'bananas']
fruit.append(fruit.pop(0))
########################################################################
# Given several lists, gather together the first element from every list, the second element from every list, and so on for all corresponding index values in the lists
first = ['Bruce', 'Tommy Lee', 'Bruce']
last = ['Willis', 'Jones', 'Lee']
years = [1955, 1946, 1940]

actors = zip(first, last, years)

assert len(actors) == 3
assert actors[1] == ('Tommy Lee', 'Jones', 1946)
################################################################################################################################################
#Given two source lists (or sets), generate a list (or set) of all the pairs derived by combining elements from the individual lists (sets)
suites = ('H', 'D', 'C', 'S')
faces = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
deck = [(face,suite) for suite in suites for face in faces]
assert len(deck) == 52
assert ('A', 'H') in deck
########################################################################
#Given a list that might contain e.g. a string, an integer, a float and a date,
#split the list into numbers and non-numbers. 
import re
data = '34234aff340980adf0e0fa0fefl' ## or ''.join(array)

nonDigits =  re.findall(re.compile('\D'), data)
digits = re.findall(re.compile('\d'), data)
#####################################################################
#Given a list, test if a certain logical condition (i.e. predicate) holds for all items of the list. 
all(x > 1 for x in [2,3,4])
#######################################################################################################################################
#Given a list, test if a certain logical condition (i.e. predicate) holds for any items of the list. 
any(x > 3 for x in [2, 3, 4])
#######################################################################################################################################
###############################################################