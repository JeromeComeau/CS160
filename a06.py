'''
This is a program by Jerome Comeau
Ths allows the user to input two values, and then sums the values
of all odd and all even integers between the two values
Date Created: 05/20/2018
'''
#import modules
import math
import operator
from statistics import mean


#ask the user for inputs
def func(n,m):
  num = range(n,m+1)
  odd = [x for x in num if x%2]
  even = [x for x in num if not x%2 and x != 0]
  return odd, even

Start = int(input('Please enter the first number: '))
Stop = int(input('Please enter the second number: '))


odd, even = func(Start,Stop)
print('The sum of all the even numbers between '+str(Start)+' and '+str(Stop)+' (inclusive) is: '+str(sum(even)))
print('The sum of all the odd numbers between '+str(Start)+' and '+str(Stop)+' (inclusive) is: '+str(sum(odd)))
