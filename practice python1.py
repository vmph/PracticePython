# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 09:37:40 2015

@author: valerie
"""

def sepa(A):
    Aeven = []
    Aodd = []
    for i in range(len(A)):
        if A[i] %2 == 0:
            Aeven.append(A[i])
        if A[i] %2 != 0:
            Aodd.append(A[i])
    Anew = sorted(Aeven) + sorted(Aodd)
    return Anew
    
A = [2,5,3,1,6,8,7]
A = [0,1,1,0,0,0,1,1,1,4,6,2,3]
sepa(A)
###############################################################################
#d1 = {'a':3, 'b':5,'c':7,'d':0, 'e':3}
##############################################################################
def f1(A):
    d = dict()
    d1 = dict()
    print "d=", d
    print "A=", A
    
    for i in range(len(A)):
        if A[i] not in d:
            d[A[i]] = 1   # value of that key is set to 1
        else:
            d[A[i]] += 1  # value of that key is incremented
    
    print ""    
    
    print "******* SEARCHING through the keys in dict**********"
    for k in d:   # loop through the keys in dict
        print "key =", k, "value of key =", d[k]
        if d[k] == 3: # if the value of that key equals 3
            print "Yeah!! found key with value = 3 and the key is =", k   
    print "d =", d
    print ""

    print "********INVERTING the dictionary: TRICKY!!!!********"
    for k in d:  # loop through the keys in dict
        val = d[k]   # define val as the value for that key
        print "key in d =", k, " and its value in d =", d[k]
        
        if val not in d1: # val is now a key in d1
            d1[val] = [k]
        else:
            d1[val].append(k)
    print "Reversed dict d1 =", d1
    print "Notice: lists can be values BUT NOT keys in dict" 
     
    print ""  
    print "***A few operations on dict******"
    print "values=", d.values()  # list of all the values
    print "keys=", d.keys()    # list of all the keys
    print "items=", d.items()   # list of tuples(k,v)
    print "check is key exists..", d.has_key(0) # verify d has a given key 

    print d.viewitems()   # just for viewing items in d , NOT a copy
    print d.viewvalues()  # just viewing the values in d
    print d.viewkeys()    # just viewing the keys in d

    print ""    
    h = d.get(0)
    print "get the value for the key 0 =", h  
    h = d.get(4)
    print "get the value for the key 4 =", h   # non existant = None
    d1 = d.copy()
    print "this is a copy of the dict=", d1
   
    return d
        
AA=[0,1,1,1,0,0,0,2,2,2]
f1(AA)
#############################################################################
# Remove duplicates in a list
def remdup(A):
    Auniq =[]
    for i in range(len(A)):  # using single pass
        if A[i] not in Auniq:
            Auniq.append(A[i])
    return Auniq

#A = [0,2,1,0,3,4,2]
A = [0,2,1,0,3,4,2,1,2,0,0,0,1,2]
remdup(A)    
##########################################################################   
def remdup2(A): ## CODE PAS EVIDENT
    A.sort()  # sort the list
    print "A=", A
    j = 0   # start at 0: index to keep track of unique elements
    print "j=", j
    print "************"
    
    for i in range(1, len(A)): # loop through the list 
        print "i=",i
        
        if A[j] != A[i]:       # IF values do NOT match
            print "found that they are not the same"
            j += 1             # increase index j by 1 
            print "j=", j
            A[j] = A[i]        # value at index j is next unique element A[i]
            print " Next unique element is =", A[j]
        
    print A[:j+1]
    
A = [0,2,1,0,3,4,2,1,2,0,0,0,1,2]
remdup2(A)        
###################################################################
# Given 2 arrays, check whether both arrays have the same set of numbers
def samenumbs(A,B):
    da=dict()
    db=dict()
    
    for i in range(len(A)): # create dictA from list A
        if A[i] not in da:  
            da[A[i]] = 1    
        else:
            da[A[i]] += 1
    
    print "da=", da
        
    for i in range(len(B)): # create dictB from list B
        if B[i] not in db:
            db[B[i]] = 1
        else:
            db[B[i]] += 1       
    print "db=", db
    
    if len(da) < len(db):     # if list A is shorter than list B
        for k1 in da.keys():  # comparing same keys
            if k1 in db.keys():
                print "yep, this key from da is in db"
        return da.keys()
    
    else:                   # if list B is shorter than list A
        for k2 in db.keys():
            if k2 in da.keys():
                print "yep, this key from db is in da"
        return db.keys()



B=[2,5,6,8,10,2,2]
A=[2,5,5,8,10,5,6,1,1,3,2,7,0]
samenumbs(A,B) 
##########################################################################
# Given 2 arrays, check whether both arrays have the same set of numbers with same occurences
def samenum2(A,B):
    da=dict()  # create 2 dictionaries
    db=dict()
    
    for i in range(len(A)): # create dict A from list A
        if A[i] not in da:  
            da[A[i]] = 1    
        else:
            da[A[i]] += 1  
            
    for i in range(len(B)):  # create dict B from list B
        if B[i] not in db:
            db[B[i]] = 1
        else:
            db[B[i]] += 1       
               
# Sorting is my best friend!!!
    print "da keys=", sorted(da.keys())
    print "db keys=", sorted(db.keys())
    print "da values=", sorted(da.values())
    print "db values=", sorted(db.values())
    print "da items=", da.items()
    print "db items=", db.items()


    if len(da) < len(db):
        for item in da.items():
            if item not in db.items():
                print "Sorry, they are not the same"
                return
        print "both arrays have the same numbers and same occurences"
        
    else:
         for item in db.items():
            if item not in da.items():
                print "Sorry, they are not the same"
                return
         print "both arrays have the same numbers and same occurences"
     
A=[0,1,1]
B=[1,0]   
samenum2(A,B)  
A=[2,2,2,3,3,3,1]
B=[2,5,5,8,10,5,6,1,1,3,2,7,0]
samenum2(A,B) 
# complexity is O(nlogn) for sorting, and O(n) for looping. so finally, O(nLogn)
###############################################################################
# Find repeated char in a string
def repstr(S):
    count = [0]*256 # initialize count list with all zeros
    print "S=", S
    print "len=", len(S)
    
    for i in range(len(S)):
        print "i=", i
        c = ord(S[i])
        print "ordinal value for char=", c
        
        if count[c]==1:  # found repeated char
            print "val=", S[i]
            print "sorry, found repeated char"
            break
        else:
            count[ord(S[i])] +=1
        
    if i == len(S)-1:
        print "No repeated char in S"

#S=['C','a','r','e','m','o','n','k']
S=['C','a','r','e','m','m','o','n','n','k']
repstr(S)
###############################################################################
# Reverse a string : Complexity O(n)
def revestr(s):
    l=list(s)
    temp = []  # using a temp variable to store let
    start=0   # index start begins at 0
    end = len(l)-1  # index end begins at len(l)-1
    while (start < end): # loop until start < end
        temp=l[start]    # first let goes to temp
        l[start]=l[end]  # first let replaced by end let
        l[end]=temp      # end let replaced by temp
        start+=1         # increment start
        end-=1           # decrement end
    return "".join(l)    # join the list into a string

s="justatry"
revestr(s)

##########################################################
def revestr1(s):  # Same but without using temp variable
    l=list(s)
    end=len(l)-1
    start=0
    while(start<end):
        l[start], l[end] = s[end], l[start]  # swapping elements
        start+=1
        end-=1
    return "".join(l) 
    
s="justatry"
revestr1(s)
#####################################################
# Another way is to use slicing syntax
s="justatry"
s1= s[::-1]
print s1
######################################################
# Even better: using reverse() method on list
s="justatry"
l=list(s)
print l
l.reverse()
print l1
##############################################
backl = reversed(l) # using built-in method reversed()
for i in backl:
    print i
######################################################
# Reversing a string of words (same as reverse a string)
def reverword(s):
    l=list(s)
    temp=[]
    start=0
    end=len(l)-1
    while(start<end):
        temp=l[start]
        l[start]=l[end]
        l[end]=temp
        start+=1
        end-=1
    return "".join(l)        
        
s="This is a testing string. THis is a lot of fun."
reverword(s)
#########################################################
# Reverse a string of words with
def reversetxt(s):   # NOT WORKING ????????????????????????
    result=[]
    inWord=False
    start=0
    for i in range(len(s)):
        if (s[i]=='' or s[i]=='\t') and inWord:
            inWord=False
            result.insert(0, s[start:i])
            result.insert(0,'')
        elif not(s[i]=='' or s[i]=='\t'or inWord):
            inWord=True
            start = i
    if inWord:
        result.insert(0, s[start:len(s)])
        result.insert(0,'')
    if len(result)>0:
        result.pop(0)
    return "".join(result)

    
s="This is a testing string. This is a lot of fun.This will teach me a lot."
reversetxt(s)     
#######################################################################
# Give all possible permutations of characters in a string
def permu(s):
    # there are n! possibilities for a string of len n

    level=[s[0]]  # create list level with first element of string
    print "level=", level
    
    for i in range(1,len(s)):
        nList=[]   # create empty list
        for item in level:
            nList.append(item+s[i])
            for j in range(len(item)):
                print "i=",i, "item=", item, "j=", j
                nList.append(item[0:j] + s[i] + item[j:])                
        level = nList
        print "level=", level
        
    print "Number of permutations equals len of nList=", len(nList)
    return nList
    
s="1234"
permu(s)
####################################################################
import time
d1="2007-07-18 10:03:19"
d1.split()[0]   # gives the date string
d1.split()[1]   # give the time string
from dateutil.parser import parse
date_obj = parse(d1)
date_obj
date_obj.strftime("%Y-%m-%d")
date_obj.strftime("%Y")  # separate the year
date_obj.strftime("%m")  # separate the month
date_obj.strftime("%d")  # separate the day
######################################################################
from sets import Set
fruits = Set(["apples","oranges","grapes","bananas"])
citrus = Set(["lemons","oranges","limes","grapefruits","clementines"])

citrus_in_fruits = fruits & citrus   #intersection
print(citrus_in_fruits)

diff_fruits = fruits - citrus        # set difference
print(diff_fruits)

diff_fruits_reverse = citrus - fruits  # set difference
print(diff_fruits_reverse)

citrus_or_fruits = citrus | fruits     # set union
print(citrus_or_fruits)

######################Lists and Sets############################################

#####To create unique list: Transform List to Set and Set back to Lits###########
a_list = ["a", "a","a", "b",1,2,3,"d",1]
print(a_list)

a_set = set(a_list)  # Convert list to set
print(a_set)         # Creates a set with unique elements

new_list = list(a_set) # Convert set to list
print(new_list)        # Obtain a list with unique elements

#############################################################################
#x=3 amd y=4, swap the values of x and y so that x=4 and y=3
x=3
y=4
print "x=",x
print "y=",y
temp=3
x=4
y=3
print "x=",x
print "y=",y
# OR ####################################
x=3
y=4
tmp = x
x = y
y = tmp
print x, y
####################################################
x=3
y=4
x,y = y, x
print x, y
#####################################################
def eucli(u,v):
    import math
# u and v are tuples (x,y), immutable
    try:
        dista = math.sqrt((u[0] -v[0])**2 + (u[1]-v[1])**2)
    except:
        if u < 0:
            print "Cannot be negative"
    return dista

eucli((3,0),(0,4))
##############################################################################
##Usign dict, calculate the numb of times each char occurs in a string
def countingstr(s):
    d = dict()
    s = s.lower()
    for el in s:
        if el not in d:
            d[el] = 1
        else:
            d[el] += 1
    print "d=", d
    print "THe number of time a appears=", d["a"]
    return
        
s = """
Write a program that prints the numbers from 1 to 100.
But for multiples of three print 'Fizz' instead of the number and f
or the multiples of five print 'Buzz'. For numbers which are
multiples of both three and five print 'FizzBuzz'
"""            
countingstr(s)
##############################################################################
#####Find numbers of sliding window of len 5 with at least 1 a in it
def slidingwindow(s):
    import string
    #Elimilate all punctuation, spaces,return carriage 
    s1 = s.lower()                              # all char to lower case
    s2 = s1.translate(None, string.punctuation) # remove all string punctuations
    s3 = s2.replace(' ', '')                    # remove spaces
    s4 = s3.replace('\n', '')                   # remove    
    
    count = 0
    start = 0
    stop = 5
    while(stop<=len(s4)):   # implementation of the sliding window of len 5
        if "a" in s4[start:stop]:
            count+=1
        start += 1   # move by 1
        stop += 1    # move by 1
    print count

s = """
Write a program that prints the numbers from 1 to 100.
But for multiples of three print 'Fizz' instead of the number and f
or the multiples of five print 'Buzz'. For numbers which are
multiples of both three and five print 'FizzBuzz'
"""            
slidingwindow(s)
######################################################
# Find the UNique numbers in LIST using dict
def findun(L):
    d=dict()
    print "the len of L =", len(L)
    print "Building a dictionary..."
    for el in L:   # adding the numbers in a dictionary
        if el not in d:
            d[el] = 1
        else:
            d[el] += 1
    print "d=", d
    print ""
    print "Next, inversing the dictionary......"
# DO reverse lookup
#Attention: some keys may have the same value!!!!    
#    for k, v in d.items(): # reversing the dictionary to find all numbers with value=1
#        if v == 1:
#            temp.append(k)
#    print "temp=", temp
#    return len(temp)
    invd=dict()
    for k in d:
        v = d[k]
        if v not in invd:
            invd[v] = [k]
        else:
            invd[v].append(k)
    print "inversed=", invd
    print ""
    print "Selecting only the element with value=1....."
    print invd[v==1]
    return len(invd[v==1])
    
L = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]    
findun(L)    
##########################################################################
#make this list with UNIQUE numbers
def findun1(L):
    L.sort()  # First, sort the List 
    print "L=", L
    L1 = Set(L) # make it unique with Set
    print "L1=", L1
    L2 = list(L1) # transform set back to a list
    print "L2=", L2
    return len(L2)
    
L = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]    
findun1(L)   
##########################################################################
def sq(x):
    return x**2
def cub(x):
    return x**3
def sith(x):
    return cub(sq(x))
def test(x):
    diff = abs(sith(x) - x**6)
    print diff
    assert(abs(sith(x) - x**6)) < 1E-6

x1=[-1,0,1.5]
for x in x1:    
    test(i)
   
######################################################################
#Create a list of the cubes of x for x in [0, 10] using
# 1)a for loop - 2)a list comprehension - 3)the map function
cubes1 = []
for i in range(1, 11):
    cubes1.append(i**3)
print cubes1

cubes2 = [i**3 for i in range(1, 11)]
print cubes2

print map(lambda x: x**3, range(1, 11))
#######################################################################
#A Pythagorean triple is an integer solution to the Pythagorean theorem a2+b2=c2. 
#The first Pythagorean triple is (3,4,5). Find all unique Pythagorean triples for 
#the positive integers a, b and c less than 100.
def pytha():
    temp=[]
    for a in range(1,100):
        for b in range(1,100):
            for c in range(1,100):
                if (a**2 + b**2) == c**2:
                    temp.append((a,b,c))
    tempun=list(Set(temp))          
    print "tempun=", tempun
    print "count=", len(tempun)

pytha()
#######################################################
pythagorean_triples = [(a, b, c) for a in range(1, 100)
                                 for b in range(1, 100)
                                 for c in range(1, 100)
                                 if a**2 + b**2 == c**2]
print pythagorean_triples
print len(pythagorean_triples)
#########################################################
# Take a list of numbers and return normalized numbers
def norma(L):
    import math

    m=sum(L)   #calculate the mean
    l=len(L)   # total 
    print "l=", l
    mn = m/l
    print"mn=", mn
    
    d = 0      # calculate the sd
    new=[]
    print "L=", L
    for i in range(len(L)):
        d += (L[i]-mn)**2
    ssd = math.sqrt(d/(l-1))
    print "ssd=", ssd 
      
    for i in range(l):
        new.append((L[i]-mn)/ssd)
    print new

norma([1,3,5,7,9])
#################################################################
###############CODING CHALLENGES from GALVANIZE#######################
# Algo to determine if str has ALL unique char
def unstr(s):
    d = dict()
    s=s.lower()
    print s
    for ch in s:   # O(n) complexity
        if ch not in d:
            d[ch]=1
        else:
            d[ch]+=1
            return False
    return True
    
s="This is a test to see if this works"
unstr(s)
# OR
def unstr(s):
    return len(set(s)) == len(s)    # O(n) complexity
###################################################################
#Determine if a string is a permutation of another 
def permustr(s1, s2):
    l1=list(s1)
    l2=list(s2)
    l1.sort()  # modifies the original list
    l2.sort()  # Beware: l22=sorted(l2) does Not modify original list
    if l1 == l2:
        return True
    else:
        return False

s1="n ibai"  # biin
s2="bini a"  # biin
permustr(s1, s2)
#####################################################################
# Determine if a string is a rotation of every letter of another
def rotatstr(s1,s2):
    l=len(s1)
    if len(s1)!=len(s2):  # immediatly if len not the same
        return False
    else:
        for i in range(l):
            if s1[i]!=s2[l-1-i]:
                return False
        return True
        
rotatstr("cha rert","trer ahc")
rotatstr("","")
########################################################################
# Determine if a string is a rotation of another ???BIZARRE
def rotat1str(s1,s2):
    if len(s1)!=len(s2):  # immediately if len not the same
        return False
    else:    
        if s2 in s1+s1:
            return True

rotat1str('foobarbaz', 'barbazfoo')
######################################################################
#Algo to compress a string 'AAABCCDDDD' becomes 'A3B1C2D4'
def compres(s):
    if s is None or len(s) == 0:
        return s
        
    temp=[]
    count=0
    L=list(s)
    tot = 0
    for i in range(len(L)-count):
        i = tot
        count=0
        for j in range(i, len(L)-count):
            if L[j]==L[i]:
                count += 1
            else:
                break         
        tot = tot + count
        temp.append(L[i])
        temp.append(str(count))
        if tot == len(L):
            break
    return "".join(temp)            

compres('AAABCCDDDD')
compres('AAFFFFFFABCCDDDRRRRD')
#############################################################################
# Reverse char in string    
def revers(s):
    if s is None or len(s)==0:
        return s
    L=list(s)
    temp=0
    mid=len(s)//2
    for i in range(0,mid):
        j = len(L)-1 - i
        if j > i:
            temp=L[i]
            L[i], L[j] = L[j], temp
        else:
            break 
    return "".join(L)
  
revers("thisisit")  # becomes "tisisiht"
revers("foo bar")  # becomes "rab oof"
##############################################################################
# implement a hash table              ##TO DO
############################################################################
#Find the first non-repeated character in a string
def nonrepeat(s):
    if s is None or len(s)==0:
        return s
    L=list(s)    
    for i in range(len(L)-1):
        if i > 1 and L[i] != L[i-1] and L[i]!= L[i+1]:
           return str(L[i])
        
nonrepeat("cchhap")            
nonrepeat("cchhaaaaopppo")          
################################################################################
#################Sorting and Searching #########################################
##################Bit Manipulation###########################################
#Given a number between 0 and 1, print the binary representation
#Determine the number of bits required to convert integer A to integer B
#Swap odd and even bits in an integer with as few instructions as possible
#Determine the number of 1 bits in the binary representation of a given integer

n=int(input('please enter the no. in decimal format: '))
x=n
k=[]
while (n>0):
    a=int(float(n%2))
    k.append(a)
    n=(n-a)/2
k.append(0)
string=""
for j in k[::-1]:
    string=string+str(j)
print('The binary no. for %d is %s'%(x, string))

################################################################################
def isAnagram(s, t):
        ds=dict()
        dt=dict() 
        for el in s:
            if el in ds:
                ds[el]+=1
            else:
                ds[el]=1
        print ds
        
        for el in t:
            if el in dt:
                dt[el]+=1
            else:
                dt[el]=1
        print dt        
        
        if ds == dt:
            return True
        else:
            return False

isAnagram("thisu", "suthi")