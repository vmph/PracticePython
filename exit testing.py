# -*- coding: utf-8 -*-
"""
Created on Fri Aug 01 11:20:54 2014

@author: Valerie
"""
def menu():
    
    user1= raw_input('Are you ready to start ?(answer: yes or no) ' )
         
    if user1 == 'no':
        user2 ='5'
            
    if user1 == 'yes': 
        print('Great, What Operation do you want to work on ? :\n')
        user2=raw_input('Select one of the following Options: 1)Addition,  5) Quit the program (Enter 1 or 5):  ')
    
    return user2
         
  
def addition(num1, num2):
    Add_res = num1+num2
    print 'the result of the addition is:', Add_res

   
# Main program starts here
loop = 1
while loop == 1:
    
    user2=menu()
    
    if user2 =='1':
          print('Ok, Let us do some additions.')
          num1 = input('Enter a first number or numerator: ')
          num2 = input('enter a second number or denominator: ')
          addition(num1, num2)
    
    elif  user2 =='5':
          print('Ok, You want to quit the program. Bye!')
          loop = 0
   
