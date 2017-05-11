# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 18:14:36 2014

@author: Anthony
"""


def menu():
    user1= raw_input('Ready to start ?(answer: yes or no) ' )
       
    if user1 == 'yes' or user1=='Yes': 
         print('Great, What Operation do you want to work on ? :\n')
         user2=raw_input('Select one of the following Options: 1)Addition, 2)Substraction, 3)Multiplication, 4)Division 5) Quit the program (Enter 1,2,3, 4 or 5):  ')
                
    if user1 == 'no' or user1=='No':
         user2='5'
    
    return user2
  
    
def addition(num1, num2):
    Add_res = num1+num2
    print 'the result of the addition is:', Add_res

def substraction(num1, num2):
    Sub_res = num1-num2
    print 'the result of the addition is:', Sub_res

def multiplication(num1, num2):
    Mult_res = num1*num2
    print 'the result of the multiplication is:', Mult_res
  
def division(num1, num2):
    while (num2==0):
        print('denominator cannot be 0, try again')
        num2 = input('enter a second number or denominator: ')
    Div_res = float(num1)/float(num2)
    print 'the result of the division is:', Div_res
    
# Main program starts here
user=raw_input('Welcome to PyCalculator! What is your name?  ')
print 'Welcome', user,'!'

loop = 1
while loop == 1:
    
        user2 = menu()
    
        if user2 =='1':
            print('Ok, Let us do some additions.')
            num1 = input('Enter a first number or numerator: ')
            num2 = input('enter a second number or denominator: ')
            addition(num1, num2)
       
        elif user2 =='2':
           print('Ok, Let us do some Substractions.')
           num1 = input('Enter a first number or numerator: ')
           num2 = input('enter a second number or denominator: ')          
           substraction(num1, num2)
          
        elif user2 =='3':
           print('Ok, Let us do some Multiplications.')
           num1 = input('Enter a first number or numerator: ')
           num2 = input('enter a second number or denominator: ')          
           multiplication(num1, num2)
          
        elif user2 =='4':
           print('Ok, Let us do some Divisions.')          
           num1 = input('Enter a first number or numerator: ')
           num2 = input('enter a second number or denominator: ') 
           while (num2==0):
               print('denominator cannot be 0, try again')
               num2 = input('enter a second number or denominator: ')
           division(num1, num2)
    
        elif user2 =='5':
            print('Ok, You want to quit the program. Bye!')
            loop = 0
   
           
          
          
          
          
    
    
    