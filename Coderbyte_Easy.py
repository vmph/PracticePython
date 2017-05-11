# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 15:11:32 2014

@author: Valerie
"""

def FirstReverse(str): 
#Reverse a string
    str=raw_input('enter a string here: ')
    newstr=str[::-1]
    print (newstr)
 
#****************************************************
def FirstFactorial(num): 
#Calculate factorial of number n
    if num == 0:
        return 1
    else:
        recurse =FirstFactorial(num-1)
        result = num*recurse
        return result 
    
    print FirstFactorial(raw_input())

#**************************************************** 
def FirstFactorial(n):
#    """ Iterative version much simpler"""
    r = 1
    for i in xrange(2, n + 1):
        r *= i
    return r

print FirstFactorial(raw_input())

#***********************************************************

def LongestWord(sen):
 return longest word in string
    longest = ""
    
    for word in sen.split():
        if word.isalpha():
            longest = word if len(word) > len(longest) else longest
    return longest

print LongestWord(raw_input())

#****************************************************
def LetterChanges(stre):
#manipulate char in a string based on position
    rv_str = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in stre:
        if ord('a') <= ord(letter) and ord(letter) < ord('z'):
            ch_str = ord(letter) + 1
            if ch_str in map(ord, vowels):
                rv_str += chr(ch_str - 32)
            else:
                rv_str += chr(ch_str)
        elif letter == 'z':
            rv_str += 'A'
        else:
            rv_str += letter
    return rv_str
print LetterChanges(raw_input())
#********************************************************
def SimpleAdding(num):
# add up all numbers from 1 to n
    sum = 0
    for num in xrange(1, num + 1):
        sum += num
    return sum

def SimpleAdding2(num):
    return reduce(lambda x, y: x + y, [n for n in xrange(1, num + 1)])


def SimpleAdding3(num):
    return sum(xrange(1, num + 1))


def SimpleAdding4(num):
    return (num * (num + 1)) / 2

print SimpleAdding(raw_input())

#************************************************
def LetterCapitalize(str): 
#Capitalize char in strings  
    lst = [word[0].upper() + word[1:] for word in str.split()]
    newstr = " ".join(lst)
    return newstr
#*********************************************OR    
    for word in str.split():
        lst = word[0].upper() + word[1:]
        print(lst)
        newstr = "".join(lst)
    return newstr
        
    
#***********************************************************    
def SimpleSymbols(str):
 char in strings and their positions
    prev = ""
    in_cmp = False
    for ch in str:
        if ch.isalpha():
            if prev != "+":
                return 'false'
            in_cmp = True
        elif prev.isalpha():
            if ch != '+':
                return 'false'
            in_cmp = False
        prev = ch
    return 'false' if in_cmp else 'true'
    # Same return expression written with and/or logic
    #return in_cmp and 'false' or 'true'

## keep this function call here
# to see how to enter arguments in Python scroll down
print SimpleSymbols(raw_input())
#*************************************************************
def CheckNums(num1, num2):
compare numbers and determine which is greater
    if num1 == num2:
        return "-1"
    return "true" if num2 > num1 else "false"


def CheckNums2(num1, num2):
    return num1 == num2 and "-1" or (num2 > num1 and "true" or "false")


# keep this function call here
# to see how to enter arguments in Python scroll down
print CheckNums(raw_input())
#*****************************************************************
#def TimeConvert(num):
 return "{hour}:{minute}".format(hour=num / 60, minute=num % 60)
#
def TimeConvert2(num):
    return str(num / 60) + ":" + str(num % 60)


# keep this function call here
# to see how to enter arguments in Python scroll down
print TimeConvert(raw_input())
#*****************************************************************
def AlphabetSoup(stre):
    return "".join(sorted(stre))


# keep this function call here
# to see how to enter arguments in Python scroll down
print AlphabetSoup(raw_input())
#*************************************************************
def ABCheck(str_):
    for i in range(0, len(str_) - 4):
        if (str_[i], str_[i + 4]) in [('a', 'b'), ('b', 'a')]:
            return "true"
    return "false"


# keep this function call here
# to see how to enter arguments in Python scroll down
print ABCheck(raw_input())
#************************************************************
def VowelCount(str_):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len([ch for ch in str_ if ch.lower() in vowels])


def VowelCount2(str_):
    vowels = ['a', 'e', 'i', 'o', 'u']
    # vowels = "aeiou"
    return len(filter(lambda x: x.lower() in vowels, str_))


# keep this function call here
# to see how to enter arguments in Python scroll down
print VowelCount(raw_input())
#***************************************************************

def WordCount(str_):
    return len(str_.split())


# keep this function call here
# to see how to enter arguments in Python scroll down
print WordCount(raw_input())
#****************************************************
# Have the function ExOh(str) take the str parameter being passed and return
# the string true if there is an equal number of x's and o's, otherwise return
# the string false. Only these two letters will be entered in the string, no
# punctuation or numbers. For example: if str is "xooxxxxooxo" then the output
# should return false because there are 6 x's and 5 o's.


def ExOh(str_):
    return "true" if str_.count('x') == str_.count('o') else "false"


def ExOh2(str_):
    return (str_.count('x') == str_.count('o')) and "true" or "false"


# keep this function call here
# to see how to enter arguments in Python scroll down
print ExOh(raw_input())
#*********************************************************
# Have the function Palindrome(str) take the str parameter being passed and
# return the string true if the parameter is a palindrome, (the string is the
# same forward as it is backward) otherwise return the string false. For
# example: "racecar" is also "racecar" backwards. Punctuation and numbers
# will not be part of the string.


def Palindrome(str_):
    cmp_str = str_.replace(" ", "")
    return cmp_str == cmp_str[::-1] and "true" or "false"


def Palindrome2(str_):
    cmp_str = ''.join(str_.split())
    return 'true' if cmp_str == ''.join(reversed(cmp_str)) else 'false'

def Palindrome(str):
    if (str == str[::-1]):
        print True
    else:
        print False
    
Palindrome('neveroddoreven')    
# keep this function call here
# to see how to enter arguments in Python scroll down
print Palindrome(raw_input())
#****************************************************************
def ArithGeo(arr):
    diff = arr[1] - arr[0]
    mult = arr[1] / arr[0]
    arithmetic = True
    for i in range(0, len(arr) - 1):
        if diff != (arr[i + 1] - arr[i]):
            arithmetic = False
            break
    if arithmetic:
        return "Arithmetic"
    for i in range(0, len(arr) - 1):
        if mult != (arr[i + 1] / arr[i]):
            return -1
    return "Geometric"


# keep this function call here
# to see how to enter arguments in Python scroll down
print ArithGeo(raw_input())
#*******************************************************************
def ArrayAdditionI(arr):
    from itertools import combinations
    max_of_arr = max(arr)
    arr.pop(arr.index(max_of_arr))
    for i in range(1, len(arr) + 1):
        for lst in combinations(arr, i):
            if max_of_arr == sum(lst):
                return "true"
    return "false"

# keep this function call here
# to see how to enter arguments in Python scroll down
print ArrayAdditionI(raw_input())
#*******************************************************************
def LetterCount(str_):
    #str = str.lower()
    maxlt_word = None
    max_lts = [(0, '')]
    for word in str_.split():
        if len(word) == len(set(word)):
            continue
        letter_list = [(word.count(letter), letter) for letter in set(word)]
        max_of_lt = max(letter_list)[0]
        if max_of_lt > 1:
            word_max_lts = filter(
                lambda x: x[0] == max(letter_list)[0], letter_list)
            if max(word_max_lts)[0] > max(max_lts)[0]:
                maxlt_word = word
                max_lts = word_max_lts
            if max(word_max_lts)[0] == max(max_lts)[0]:
                if len(word_max_lts) > len(max_lts):
                    maxlt_word = word
                    max_lts = word_max_lts

    return maxlt_word or -1


# keep this function call here
# to see how to enter arguments in Python scroll down
print LetterCount(raw_input())
#***********************************************************************







