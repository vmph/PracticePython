# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:06:06 2015

@author: Valerie
"""
# Translate a txt where each letter becomes the letter + 2counts of letter
# txt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj." 
# txt1= "g fmnc wms bgblr rpylqjyrc gr"
def readpuzzle(txt):
    let = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    txtl=list(txt)
    ll = len(txtl)
    print "ll=", ll
    print " txtl=", txtl
    
    for i in range(len(txtl)):
        print "i= ", i
        
        if txtl[i] == 'y':                 #take care of the second to last char
            txtl[i] = 'a'                  # manually
            print "found case 1: y becomes ", txtl[i]                   
        elif txtl[i] == 'z':               # take care of the last char  
            txtl[i] = 'b'                  # manually
            print "found case 2: z becomes ", txtl[i]
        else:                              # all other char
            for j in range(len(let)-2):    # automate
                print "letter =", txtl[i]
                if txtl[i] == let[j]:
                    txtl[i] = let[j+2]
                    print "letter becomes ", let[j+2]
                    break
            
    txtnew = "".join(txtl)
    return txtnew
################################################################################
# Use ord() to convert a single character to its corresponding ASCII value.
# Use chr() to convert an ASCII value to its corsponding character 
import string
vals = string.letters
print "vals=", vals
num=5
for i in vals:
    print i, ord(i), chr(ord(i)), ord(i) + num, chr(ord(i)+num)
##############################################################################    
string='Hello World'
list_ascii=[ord(i) for i in string] 
print list_ascii    
###############################################################################
list_ascii=[72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
list_char=[chr(i) for i in list_ascii]
print list_char
str1=''.join(list_char)
print str1 
################################################################################
def rotate_word(txt,num): # Return new string that contains the letter rotated by the given amount
    import string
    vals = string.letters

    result = ""
    for item in txt:
        if item in vals:
            c = ord(item) + num
            if ord(item) != c: # why do we need this ???
                b = chr(c)
                result += b
        else:
            result += item
    print result
        
    
rotate_word("abord mission, dont atk teacher!",5)    


###############################################################################
def rotate_word(txt,num): # Return new string that contains the letter rotated by the given amount
    import string
    vals = string.letters

    result = ""
    for item in txt:
        if item in vals:
            c = ord(item) + num
            b = chr(c)
            result += b
        else:
            result += item
    print result
        
###########################################################    
def RotateMe(text,mode=0,steps=1):  # Takes a string and rotates the characters by the number of steps.
    length=len(text)
 
    for step in range(steps):
        print "step=", step
 
        if mode==0:    # rotate right
            text = text[length-1] + text[0:length-1]  # last char + string up to not includ last char
            print "text=", text
        else:          # rotate left
            text = text[1:length] + text[0]   ## string up to last char + first char
 
    return text
###############################################################

################################################################################### 
###############EXERCISES FROM CRACKING THE CODE INTERVIEW#########################           
#create a script that will check if a string has unique characters
def checkstr(s):
    l = list(s)
    for i in range(len(l)):
        for j in range(len(l)):
            if i!=j and l[i]==l[j]:
                return False
    return True
#######################################################
# create a script that will compress a string from "aabbbccdaaabb" into "a2b3c2a3b2"
      
##########################    
def histoletter(s):    
    dd = {}
    for let in s:
        if let not in dd:
            dd[let] = 1
        else:
           dd[let] += 1
    return dd
 ##############################################################################
def compressing(s):
    l = list(s)
    l1 = []

    if len(l) == 0: # if string is empty
        return 0    # return 0
    if len(l)==1:   # if string len is 1
        return s + "1" # return the char + 1
    
    count = 1 
    i = 0
    while i < len(l):  
        print "#####i=", i
        count = 1
        for j in range(len(l)):
            print "j=",j
            if j > i and l[i] == l[j]:
                print "found same letter"
                count += 1
                print "count=", count
                print ""
            if j > i and l[i] != l[j]: 
                print " letters not the same, stop and move on"
                break
        l1.append(l[i])
        l1.append(str(count))
        print "l1=", l1
        i = i + count
     
    s1 = "".join(l1)
    print "s1=", s1
    print "Original string = ", s
    print "Compressed string = ", s1
    return s1           
##################################################################################    
# same as above without the print statements
def compressing1(s):
    l = list(s)
    l1 = []

    if len(l) == 0: # if string is empty
        return 0    # return 0
    if len(l)==1:   # if string len is 1
        return s + "1" # return the char + 1
    
    i = 0           # initialize index
    while i < len(l):  # start looping through string char
        count = 1              # initialize counter to 1 to count for first str char  

        for j in range(len(l)): # loop thru string and search for matching letters
            if j > i and l[i] == l[j]: # if any 2 matching letters found for j >i
                count += 1            # increase a counter for the number of the matching letters  
            if j > i and l[i] != l[j]: # if any 2 letters are not matching   
                break                  # do not continue and break out of loop  

        l1.append(l[i])                #append that letter found
        l1.append(str(count))          # append the final count value for the number of matching letter
        i = i + count                  # increment i by the count value    
    
    s1 = "".join(l1)                   # join letter in list format back into string format
    return s1                          # return final string
################################################################################    
#write a function strRemove(s1,s2) that will delete given char s2 that exists in a string s1 
def strRemove(s1,s2):
    for ch in s1:
        if ch == s2:
            print "found "
            del ch
    return s1
    
########################Traversing a string with index and counts###############    
def find0(word, let):
    i=0
    while i < len(word):
        if word[i] == let:
            return i  # as soon as  you found let, stop and return corresponding index
        i+=1
    return -1         # if no let found, retunr -1 
##############################
def find1(word, let):  # same as above but return replaced by print
    i=0
    while i < len(word):
        if word[i] == let:
            print i    # if you found let, print the index and continue increnting
        i += 1
###############################    
def find2(word, let):  # same as find1 with for loop
    for i in range(len(word)):
        if word[i] == let:
            print i
################################    
def find3(word, let):  # same as find1 with for loop and counter added 
    count =0               # adding a counter  
    for i in range(len(word)):
        if word[i] == let:
            print i
            count+=1    
    return count
###############################################################################
def is_reverse(word1, word2): # check is word1 is the reverse of word2 and vv
    if len(word1)!= len(word2): # check both length right away
        return False
    
    i=0             # index i goes up word1
    j=len(word2)-1  # index j goes down word2
    while j >= 0:     # j cannot be negative 
        print i, j
        if word1[i] != word2[j]:  # if you find 2 letter that are not the same
            return False          # retunr False
        i+=1                      # go up with i
        j-=1                      # go down with j
    return True
###############################################################################
# string="" # create empty string
# string.find(s, sub[, start[, end]])
# string.count(s, sub[, start[, end]])
#string.lower(s)
#string.upper(s)
#string.capitalize(word)
#string.capwords(s[, sep])
#string.split(s[, sep[, maxsplit]])
#string.join(words[, sep])
#"".join(list)
#string.lstrip(s[, chars])
#string.rstrip(s[, chars])
#string.strip(s[, chars])
#string.swapcase(s)
#string.replace(s, old, new[, maxreplace])
##############################################
# list=[] # create empty list    
#list.append(x) # append element x at end of list
#list.extend(L) # extend by list L
#list.insert(i,x) # insert elementx a t index i
#liust.remove(x) #removes item of value x 
#list.pop()  # removes the last item
#list.index(x) # return index of first item of value x
#list.count(x) # return number of times x appears
#list.sort()
#list.reverse()
#del list[i]
#del list[i:j]
#del list[:]
#del list
##################################################
#Tuples are immutables 
#tup =() # create empty tuple
################################################
#Sets are unordered collections with NO duplicates
#set1 = set()
#se1 = set("asdasdfgh") # return unique elements of string
#se2 = set(["a","b","a","c","a"]) # return unique element of list    
#se1 - se2 # element in se1 not in se2
#se1 | se2 # elements in either se1 or se2
#se1 & se2 # elements in both se1 and se2
#se1 ^ se2 # elements in se1 or se2 but not both   
# set comprehension    
    
    
####################################################    
# Dictionnaries # unorderd set of unique keys:value pairs
# dict = {} # create empty dictionary
#list(d.keys()) # return list of all keys unordered
#sorted(d.keys()) # return sorted list of all keys  
# looping techniques in dictionary
    
    
#################################################
# List Comprehension : create list from sequences
    






      
# write a function that performs binary addition on two input strings.

# write a function that check if 2 strings are anagrams with each other

# reverse a string per word   
    
# replace all single occurences of "a" with "the"    
    
# write a function to check is string is palindrome
#################################################################################################
# write a function that reverses the words in a string (cats and dogs) becomes (stac dna sgod)
def reversingX(s):  # this works but it is a bit complicated
    l=list(s)

    if len(l) == 0: # if string is empty
        return 0    # return 0
    if len(l)==1:   # if string len is 1
        return s

    snew=""
    stot = ""
    lnew=[]    
    countlet = 0
    i = 0
    while i < len(l):
        countlet = 0
        print "################ i=", i

        for j in range(i, len(l)):
#            print "j=", j
            countlet += 1
            print "j=", j, "countlet=", countlet
            if l[j] == ' ':
                print "found a break at pos =", j
                print "found a word with ", countlet-1, "letters" 
                lnew = l[i:i+countlet-1]
                print "the word is", lnew
                print "the reversed word is ", lnew[::-1]
                snew = "".join(lnew[::-1])
                stot = stot + snew + " "                       
                break
            if j == len(l)-1:
                print "found last letter"
                lnew = l[i:len(l)]
                print "the word is", lnew
                print "the reversed word is ", lnew[::-1]
                snew = "".join(lnew[::-1]) 
                stot = stot + snew
                print "stot = ", stot
                break

        i = i + countlet
        print "i becomes ", i

    print "s was = ", s    
    print "The reversed words in string =", stot    
    return stot
################################################################################
def reversingX1(s):  # same as above without print statements
    l=list(s)

    if len(l) == 0: # if string is empty
        return 0    # return 0
    if len(l)==1:   # if string len is 1
        return s

    snew=""
    stot = ""
    lnew=[]    
    countlet = 0
    i = 0
    while i < len(l):
        countlet = 0

        for j in range(i, len(l)):
            countlet += 1

            if l[j] == ' ':
                lnew = l[i:i+countlet-1]
                snew = "".join(lnew[::-1])
                stot = stot + snew + " "                       
                break
            if j == len(l)-1:
                lnew = l[i:len(l)]
                snew = "".join(lnew[::-1]) 
                stot = stot + snew
                break

        i = i + countlet

    return stot
################################################################################ 
def reversing(s):  # can I do it with only one index ??????
    l=list(s)
    
    if len(l) == 0: # if string is empty
        return 0    # return 0
    if len(l) == 1:   # if string len is 1
        return s
    
    stot = ""
    lnew = []    
    countlet = 0
        
    for i in range(len(l)):
        countlet += 1
        print "i=", i, "countlet=", countlet
        
        if l[i] == ' ':
            print "found a break at pos =", i
            print "found a word with ", countlet-1, "letters" 
            lnew = l[:countlet-1]
            print "the word is", lnew
            print "the reversed word is ", lnew[::-1]
            snew = "".join(lnew[::-1])
            stot = stot + snew + " " 
            print "stot=", stot               ###NOT WORKING NEED Count1 and count2       
                   
        if i == len(l)-1:
            print "found last letter"
            lnew = l[:len(l)]
            print "the word is", lnew
            print "the reversed word is ", lnew[::-1]
            snew = "".join(lnew[::-1]) 
            stot = stot + snew
            print "stot = ", stot
            break
              
        i = i + countlet
    
    print "s was = ", s    
    print "The reversed words in string =", stot    
    return stot
##########################################################################       
def lone_sum(a, b, c):

    if a!=b and a!=c and b!=c:
        sum = a+b+c
    if a==b==c:
        sum = 0
    
    if a==b and a!=c and b!=c:
        sum = c
    elif a==c and a!=b and b!=c:
        sum = b
    else:
        sum = a    
    
    return sum        
#######################################################################        















############################################################################################

# write a function that reverse the words in sentence (I am a fool) becomes (I ma a loof)   

# given a sentence containing anagrams, find anagrams pairs and print them

# write code that print all combination s of a string    

# Write code to remove duplicate from a string

# given two arrays of char, find longest common substring    
    
    
    
    
    
    
    
    
    
    
    
    