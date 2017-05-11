# -*- coding: utf-8 -*-
"""
Created on Sat Apr 04 22:56:25 2015

@author: Valerie
"""
#####################################################################################
######################### CODINGBAT Warm-up-1######################################
###################################################################################
def sleep_in(weekday, vacation):
    if not weekday and not vacation:
        return True
    if weekday and not vacation:
        return False
    if not weekday and vacation:
        return True
    if weekday and vacation:
        return True

def sleep_in1(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

def sleep_in2(weekday, vacation): 
    return(not weekday or vacation)
#################################################
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    if a_smile and not b_smile:
        return False
    if not a_smile and b_smile:
        return False
################################################
#Given two int values, return their sum. Unless the two values are the same, then return double their sum 
def sum_double(a, b):
    if int(a)==int(b):  # need int here because a==b return booleen
        return 2*(a+b)
    else:
        return (a+b)    
###############################################################################
def diff21(n):
    if int(n) <= 21:
        return abs(n-21)
    else:
        return 2*abs(n-21)
#################################################################################
def monkey_trouble(talking, hour):
    if talking and (hour < 7 or hour >20):
        return True
    else:
        return False
#################################################################################
def makes10(a, b):
    if int(a) == 10 or int(b) == 10: 
        return True    
    elif (int(a) + int(b)) == 10:
        return True
    else:
        return False
##############################################################################
def near_hundred(n):
    if abs(100-int(n)) <= 10 or abs(200-int(n)) <= 10:
        return True
    else:
        return False  
##################################################################################
# Given 2 int values, return True if one is negative and one is positive. 
# Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
    if not negative and int(a) >0 and int(b) <0:
        return True
    elif not negative and int(b) >0 and int(a) <0:
        return True
    elif negative and int(a) <0 and int(b) <0:
        return True
    else:
        return False        
################################################################################    
def not_string(str):
    if "not" in str:
        return str
    else:
        return "not" + " " + str  
#################################################################################
def not_stringa(str):
    if str[0:3] == "not":
        return str
    else:
        return "not" + " " + str 
#################################################################################
def missing_char(str, n):
    # cannot use - or pop() or remove() or del() on strings!!!
    # string are IMMUTABLE!! need to create a new one
    l1 = list(str)  # transform str into a list
    del l1[int(n)]  # delete desired element
    str1="".join(l1) # join the list element back into a string
    return str1  # return the new string
#################################################################################
def missing_char1(str, n):
    front = str[:n]   # up to but not including n
    back = str[n+1:]  # n+1 through end of string
    return front + back        
################################################################################
def front_back(str):  # swaping 2 indices in a string
    if len(str) <= 1:
        return str
    else:
        l1 = list(str)   # transform str into list
        l1[0], l1[len(str)-1] = l1[len(str)-1], l1[0]  # swap the 2 indices in list
        return "".join(l1)   # rejoin list into a str  
##################################################################################
def front3(str):
    if len(str) < 3:
        l0 = list(str)
        return "".join(l0) + "".join(l0) + "".join(l0)
    else:
        l1 = list(str)
        front = l1[0:3]
        str1 = "".join(front) + "".join(front) + "".join(front)
        return str1
#################################################################################
# CODINGBAT Warm-up-2
def string_times(str, n):
# Given a string and a non-negative int n, return a larger string that is n copies of the original string.   
    l1 = list(str) # transform str into list
    l2 = n* l1     # perform multiplication on list
    str1 = "".join(l2) # rejoin list into a string
    return str1                 
###############################################################################
def front_times(str, n):
    if len(str) < 3:
        l1 = list(str)  # transform str into list
        l2 = n * l1     # perform operation on list
        str1 = "".join(l2)  # join list back into string
        return str1     # return new string
    else:
        l11 = list(str) # transform str into list
        front = l11[0:3]  # select element of list
        copyfront = n * front  # perform operation on selected elements into new list
        str11 = "".join(copyfront) # join new list back into string
        return str11
#################################################################################
#Given a string, return a new string made of every other char starting with the first        
def string_bits(str):
    l1 = list(str)
    le = len(l1)
    str1 = "".join(l1[0:le:2] ) 
    return str1
#################################################################################
#Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
    l1 = list(str)   # transform str into list
    newl = []       # define new empty list
    for i in range(len(l1)+1):  # loop over the range of list l1
        newl += l1[:i]   # add each sublist into newlist
    str1 = "".join(newl)  # join newlist back into a string
    return str1 
###############################################################################    
# Given a string, return the count of the number of times that a substring 
# length 2 appears in the string and also as the last 2 chars of the string
def last2(str):
    if len(str) <2:
        return 0
        
    l1 = list(str)  # transform str into a list
    count = 0      # counter to 0
    last2 = l1[len(l1)-2:len(l1)]  # sublist defined w/ last 2 elements of l1    
    for i in range(len(l1)+1):   # loop through every element of l1 
        if l1[i:i+2]  == last2:  # to search of 2 consecutive elements are identical to last2
            count += 1        # increase count
    return count-1            # return count -1 (bc over counting by 1) 
###############################################################################
# A list is an ordered collection of items which can be of ANY type. Lists are mutable.
# An array is an ordered collection of items of a "single" type.
###############################################################################
# Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
    count = 0
    for i in nums:  # loop thru the elements of the array nums
        if i == 9:  # search for the element 9
            count += 1  # increment counter
    return count
#############################################################################
#Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
#The array length may be less than 4    
def array_front9(nums):
    first4 = nums[0:4]   # define the first 4 elements of array into a sublist 
    for i in range(len(first4)):  # loop thru element of sublist
        if nums[i] == 9:  # search for 9
            return True   # return True
    return False          # otherwise False 
###############################################################################
#Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere
def array123(nums):
    for i in range(len(nums)+1):  # loop thru the len of array
        if nums[i:i+3] == [1,2,3]: # search for any sub-array of size 3 that equals [1,2,3]
            return True  # return True otherwise False
    return False 
##############################################################################
# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
def string_match(a, b):  # beware that a and b may be of different length!!
    la = list(a)  # transform string a into list la
    lb = list(b)  # transform string b into list lb
    count = 0
    for i in range(len(la)-1): # loop thru list la from 0 to len(la)-2! because of [i:i+2]
        for j in range(len(lb)-1): # loop thru list lb from 0 to len(lb)-2! because of [j:j+2]
             subla = la[i:i+2] # 2 consecutive elements in subla
             sublb = lb[j:j+2] # 2 consecutive elements in sublb
             print "sub la=", subla, "sub lb=", sublb 
             if subla == sublb and i==j: # if the sub lists are the same and are found at same position
                 count += 1  # increase counter
                 print "count=", count
    return count

##################################################################################
############################### CODINGBAT String-1###########################################
################################################################################
#Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
def hello_name(name):
    addstart = "Hello"
    addend = "!"
    return addstart + " " + name + addend  
##################################################################################
#Given two strings, a and b, return the result of putting them together in the order abba
def make_abba(a, b):
    return a+b+b+a
################################################################################
# Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>"
def make_tags(tag, word):
    sim1left = "<"
    sim1right = ">"
    sim2 = "/"
    newtag = sim1left+tag+sim1right+word+sim1left+sim2+tag+sim1right  
    return newtag    
################################################################################
def make_out_word(out, word):  # out is of len 4
    start = out[:2]  # create substring from 0 to 2
    end = out[2:]    # create substring from 2 to 4
    newword = start + word + end # create new string
    return newword
##############################################################################
#Given a string, return a new string made of 3 copies of the last 2 chars of the original string.    
def extra_end(str):
    last = str[-2:]
    new = last + last + last 
    return new 
################################################################################
# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". 
def first_two(str):
    if len(str) < 2:
        return str
    else:
        start = str[:2]
        return start
##############################################################################
# Given a string of even length, return the first half.
def first_half(str):
    l=len(str)
    first = str[:l/2]  # because str is even!!
    return first 
##################################################################################
#Given a string, return a version without the first and last char
def without_end(str):
    l=list(str) # str are immutable, so transform str into list
    del l[0]  # delete first element
    del l[-1] # delete last element
    newstr = "".join(l) # rejoin the list into a new str
    return newstr
#############################################################################           
#Given 2 strings, a and b, return a string of the form short+long+short, 
#with the shorter string on the outside and the longer string on the inside
def combo_string(a, b):
    la=len(a)  # measure len of a
    lb=len(b)  # measure len of b
    if la < lb: # check which len is smallest
        return a+b+a
    else:
        return b+a+b
#############################################################################
# Given 2 strings, return their concatenation, except omit the first char of each. 
def non_start(a, b):
    la = list(a)  # strings are immutable, so transform a into list la
    lb = list(b)  # strings are immutable, so transform b into list lb
    del la[0]     # delete first element of la
    del lb[0]     # delete first elelemt of lb
    newl = la + lb  # create new list
    newstr ="".join(newl) # join newlist into a newstring
    return newstr 
##############################################################################
#Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.    
def left2(str):
    l=list(str)
    first2 = l[0:2]
    remain = l[2:]
    newl = remain + first2
    newstr = "".join(newl)
    return newstr
#################################################################################
def left2a(str):
  return str[2:] + str[:2]

###############################################################################
################################## CODINGBAT List-1#################################
################################################################################
#Given an array of ints, return True if 6 appears as either the first or last element in the array.
def first_last6(nums):
    if nums[0]== 6 or nums[-1] == 6:
        return True
    else:
        return False
##############################################################################
#Given an array of ints, return True if the array is length 1 or more, 
# and the first element and the last element are equal. 
def same_first_last(nums):
    if len(nums) >=1 and nums[0] == nums[-1]:
        return True
    else:
        return False
#############################################################################
#Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}. 
def make_pi():
    return [3,1,4]  
###############################################################################
#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.        
def common_end(a, b):
    if a[0]==b[0] or a[-1]==b[-1]:
        return True
    else:
        return False  
##############################################################################
#Given an array of ints length 3, return the sum of all the elements. 
def sum3(nums):
    return sum(nums) 
################################################################################
#Given an array of ints length 3, return an array with the elements "rotated left" 
# so {1, 2, 3} yields {2, 3, 1} : TRICKY!!!!
def rotate_left3(nums):
    new=[]  # define an empty list
    for i in range(len(nums)-1):  #loop thru elements of nums up to len(nums)-1!!!
        new.append(nums[i+1])     # append each element to new
    new.append(nums[0])           # last element to append is first element of nums
    return new              
##################################################################################
# Given an array of ints length 3, return a new array with the elements in reverse order, 
# so {1, 2, 3} becomes {3, 2, 1}.    
def reverse3(nums):
    new= nums[::-1]  # works on odd and even lists
    return new
#################################################################################
def reverse3a(nums):
    new=[]
    for el in reversed(nums):
        new.append(el)
    return new        
#################################################################################        
#Given an array of ints length 3, figure out which is larger between the first and 
#last elements in the array, and set all the other elements to be that value. Return the changed array. 
def max_end3(nums):
    new = []                    # define new empty list
    mm = max(nums[0], nums[len(nums)-1])  # find maximum of first & last elements
    for i in range(len(nums)):
        new.append(mm)
    return new
#################################################################################
#Given an array of ints, return the sum of the first 2 elements in the array. 
# If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0
def sum2(nums):
    if len(nums)==0:
        return 0
    elif len(nums) <2:
        return sum(nums)
    else:
        su2=nums[0] + nums[1]
        return su2
##################################################################################
#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements. 
def middle_way(a, b):
    mida = a[len(a)//2]    # division must be //   
    midb = b[len(b)//2]
    new = []
    new.append(mida)  # append() takes only 1 argument at a time
    new.append(midb)
    return new 
########################################################################
# Given an array of ints, return a new array length 2 containing the first and last elements from the original array.        
def make_ends(nums):
    first = nums[0]
    last = nums[len(nums)-1]
    new=[]
    new.append(first)
    new.append(last)
    return new 
###############################################################################
#Given an int array length 2, return True if it contains a 2 or a 3.     
def has23(nums):
    if 2 in nums:
        return True
    elif 3 in nums:
        return True
    else:
        return False

###############################################################################
######################### CODINGBAT - String 2 (Medium) ##########################       
##############################################################################
#Given a string, return a string where for every char in the original, there are two chars. 
def double_char(str):
    l=list(str)
    newl =[]
    for el in l:
        newl.append(el)
        newl.append(el)
    newstr = "".join(newl)
    return newstr        
###############################################################################        
def double_char1(str):
  result = ""
  for i in range(len(str)):
    result += str[i] + str[i]
  return result        
#############################################################################        
#Return the number of times that the string "hi" appears anywhere in the given string. 
def count_hi(str):
    count = 0
    print "len of str is ", len(str)
    for i in range(len(str)-1): # I don't get why len(Str)-1!!!!!!!!!!!!!!
        print "i=", i, "i-i+2=", str[i:i+2]
        if str[i:i+2] == "hi":
            count += 1
    return count         
################################################################################        
#Return True if the string "cat" and "dog" appear the same number of times in the given string.         
def cat_dog(str):
    countc=0
    countd=0
    
    for i in range(len(str)-2):
        if str[i:i+3] == "cat":
            countc += 1
        if str[i:i+3] == "dog":
            countd +=1
            
    if countc == countd:
        return True
    else:
        return False
##############################################################################        
# Return the number of times that the string "code" appears anywhere in the given string, 
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.         
def count_code(str):
    count = 0
    al = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(str)-3):
        if str[i:i+2] == "co" and str[i+2:i+3] in al and str[i+3:i+4]=='e':
            count += 1
    return count
##################################################################################
#Given two strings, return True if either of the strings appears at the very end of the other string, 
#ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
#Note: s.lower() returns the lowercase version of a string.
def end_other(a, b):
    lowa = a.lower()
    lowb = b.lower()  
    la = len(lowa)
    lb = len(lowb)
    if la <= lb and lowa == lowb[-la:]:
        return True
    elif lb <= la and lowb == lowa[-lb:]:
        return True
    else:
        return False        
###############################################################################        
def end_other1(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))        
###############################################################################        
#Return True if the given string contains an appearance of "xyz" where the xyz 
# is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.         
def xyz_there(str):
    if str[0:3] == "xyz":
        return True
    for i in range(1, len(str)-2):
        if str[i:i+3] == "xyz" and str[i-1:i] != ".":
            return True
                
    return False

################################################################################        
############################ CODINGBAT - List 2 (Medium)##############################            
###############################################################################
#Return the number of even ints in the given array. 
# Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.         
def count_evens(nums):
    count = 0
    for el in nums:
        if el%2 == 0:
            count += 1  
    return count
#############################################################################
#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
def big_diff(nums):
    maxn = max(nums)
    minn = min(nums)
    diff = maxn - minn
    return diff
#############################################################################
#Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the array. 
# If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value.
def centered_average(nums):   
    sum = 0
    snums = sorted(nums)  # sort the list
    if snums.count(snums[0]) >= 1 or snums.count(snums[len(snums)-1]) >=1:  # if lowest and highest el are counted 1x or more
        del snums[0]  # delete one of the lowest element
        del snums[len(snums)-1]  # delete one of the highest element
    for i in range(len(snums)):  # loop thru the el of remaining list
        sum += snums[i]          # sum all the elements 
    sumavg = sum//int(len(snums))  # divide by the number of elements
    return sumavg                  # return the avg
##############################################################################    
#Return the sum of the numbers in the array, returning 0 for an empty array. 
# Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.     
# try this a= [1,13,4,5,6,13,13,13,2,13]
# sum13([13, 1, 2, 13, 2, 1, 13]) 
def sum13(nums):
    if len(nums) == 0:
        return 0
    
    sum = 0
    print "len=", len(nums)
    print ""
    
    for i in range(len(nums)):
        print "i=", i
        
        if nums[i] == 13 and i < len(nums)-1: # if el is 13 and not the last el
            print "found 13!"
            nums[i] = 0  # replace element of value 13 by 0
            nums[i+1] = 0 # replace next element value by 0
            print "nums=", nums
            sum += nums[i]  # produce sum
            print "sum=", sum
            
        elif nums[i] == 13 and i == len(nums)-1: # if el is 13 and the last el
            nums[i] = 0 # if last element value is 13, replace by 0
            print "nums=", nums
            sum += nums[i]  # produce sum
            print "sum=", sum
            
        else:   # all else
            print "nums=", nums
            sum += nums[i]  # produce sum
            print "sum=", sum
             
    return sum  
 #############################################################################   
#Return the sum of the numbers in the array, except ignore sections of numbers starting 
# with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
# a= [1,2,6,8,7,2,6,6,7,8,6]
def sum67(nums):
    if len(nums)==0:
        return 0
    print "nums=", nums    
    new = []    
    sum=0    
    for i in range(len(nums)):
        print "i =", i
        print ""
        if nums[i] == 6 and i < len(nums)-1: 
            print "found a 6 at i=", i
            for j in range(i,len(nums)):
                print "j =", j
                if nums[j] == 7:
                    print "found a 7 at j=", j
                    new = [0] * (j+1-i)
                    print "new=", new
                    nums[i:j+1] = new
                    print "nums=", nums
                    break
                             
            sum += nums[i] 
            print "sum=", sum
        elif nums[i] == 6 and i == len(nums)-1:
            print "found 6 at the very end"
            nums[-1] = 0
            print "nums=", nums
        else:
            sum += nums[i]
            print "sum=", sum
    return sum
            
###############without the print statements###############################               
def sum67a(nums):
    if len(nums)==0:
        return 0

    new = []    
    sum=0    
    for i in range(len(nums)):
        if nums[i] == 6 and i < len(nums)-1: 
            for j in range(i,len(nums)):
                if nums[j] == 7:
                    new = [0] * (j+1-i)
                    nums[i:j+1] = new
                    break                           
            sum += nums[i] 
        elif nums[i] == 6 and i == len(nums)-1:
            nums[-1] = 0
        else:
            sum += nums[i]

    return sum        
   
##############################################################################
#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere. 
# b= [1,2,6,8,7,2,6,6,7,2,2,8,6]
def has22(nums):
    flag =False    
    if nums[:2] == [2,2]:        # check the first two elements
            flag = True            
    if nums[-2:] == [2,2]:       # check the last two elements
            flag = True        
    
    for i in range(len(nums)-2):  # general case
        if nums[i:i+2] == [2,2]: 
            flag = True

    return flag
###############################################################################
 
 
# slicing in list
#a[:]                
#a[low:]             
#a[:high]            
#a[low:high]        
#a[::stride]        
#a[low::stride]      
#a[:high:stride]    
#a[low:high:stride]
#a[-1]
#a[:-2]
#a[-2:]
#a[1:1] = []
#a[1:1] = [4,4] # will add element 4 in position 1
#a[0] = a[-len(a)]
#a[len(a)-1] = a[-1]
#a[i] = a[-len(a)+i] 
#a[:] = a[0:len(a):1]  # a +1 step is the default
#a[::2] = a[0:len(a):2] # all even positions
#a[1::2] # all the odd positions    
#a[::3]  # all th multiples of 3
#a[6:2:-1] # moving backwards 
#a[::-1] = a[-1::-1]
#a[::-2] = a[-1:-len(a)-1:-2]
#a[::3] = a[-1:len(a)-1:-3]  
#sl=sline(0,4)
#a[sl] = a[0:4]
# n1 = [0 for i in range(15)]
#n2 = [0] * 15
#a = []  # empty list
#b = list()  # empty list
###################################################################################


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        