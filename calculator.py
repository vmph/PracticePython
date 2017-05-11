# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 11:07:34 2014

@author: Valerie
"""
import math
from sys import exit

count = 0
while count != 5:
      user=raw_input('what is your name?  ')
      print 'Welcome', user,'!'

 
      user1= raw_input('Do you want to use the calculator program ?(answer: yes or no) ' )

#answer = None
#while True:       
#      if answer in ("yes", "no"): break
#         print('That is not a yes or a no')
     
      if user1 == 'no':
         print('Ok, you want to quit. Bye!')
         break
       
      if user1 == 'yes': 
          print('Great, let us start!.\n')
          
          user2=raw_input('First choose which Operation you want to work on :\n Option 1: Add, Option 2: Substract, Option 3: Multiply, Option 4: Divide, Option 5: Quit Program (Just enter 1,2,3,4 or 5): ')

      if user2 =='1':
          print('Ok, Let us do some additions.')

          num1 = int(raw_input('Enter a first number: '))
          num2 = int(raw_input('enter a second number: '))
          Add_res = num1+num2
          print 'the result of the addition is:', Add_res
    
      elif user2 =='2':
          print('Ok, Let us do some Substractions.')
    
          num3 = int(raw_input('Enter a first number: '))
          num4 = int(raw_input('enter a second number: '))
          Sub_res = num3-num4
          print 'the result of the addition is:', Sub_res
 
      elif user2 =='3':
          print('Ok, Let us do some Multiplications.')
         
          num5 = int(raw_input('Enter a first number: '))
          num6 = int(raw_input('enter a second number: '))
          Mult_res = num5*num6
          print 'the result of the Multiplication is:', Mult_res
        
      elif user2 =='4':
          print('Ok, Let us do some Divisions.')
        
          num7 = int(raw_input('Enter a first number: '))
          num8 = int(raw_input('enter a second number: '))
          Div_res = num7/num8
          print 'the result of the addition is:', Div_res
   
      elif user2 =='5':
           
          count = int(user2)
          print('Ok, You want to quit the program. Bye!')
              
      else:
          print('Ok, I quit. Bye!.')
#    
#
#
