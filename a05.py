'''
This is a program by Jerome Comeau
It allows the user to insert values for grades by gender
and then figure out the average of the total
Date Created: 05/09/2018
'''
#import modules
import math
import operator
from statistics import mean


#define default values
Boys = []
Girls = []
user_input = 'A'
allowed = ['B','G','Q']
#define allowable operators
while user_input not in allowed:#only allow B, G, or Q (upper or lowercase); keep asking until one of those values is entered
    user_input = str.upper(input("Please select Boy (b), Girl (g), or Quit (q): "))#force the string to uppercase for simplicity   
else:
    while user_input != 'Q': #check to see if the value is "quit"
        if user_input == 'B': #it's not Q, so is it b? if so ask for a score for a boy
            score_b = int(input('Boy score: '))
            Boys.append(score_b) #add the value into the Boys list
            user_input = str.upper(input("Please select Boy (b), Girl (g), or Quit (q): "))#don't forget to ask for another input   
        else:
            score_g = int(input('Girl score: '))#if it's not q and it's not b, then it has to be g
            Girls.append(score_g) #add the value into the Girls list
            user_input = str.upper(input("Please select Boy (b), Girl (g), or Quit (q): "))#check to see if we're done   
    else: #if the value is Q then we're finished, so do some math
        boy_total = float(mean(Boys)) #we want a decimal, so force the float
        print('Boy Average is: '+ str(boy_total)) 
        girl_total = float(mean(Girls))
        print('Girl Average is: ' + str(girl_total))
