'''
This is a program by Jerome Comeau
It allows the user to insert integers and then 
it sums the total
Date Created: 06/03/2018
'''

#import modules
import math #because always import math
numlist = []
allowed = ['1','2','3','4','5','6','7','8','9']
def digital(numinput):
    if str.isdigit(numinput) == False:
        raise ValueError('"%s" is not a valid integer.' % numinput)

def results(numinput):
    for n in numinput[:-1]:
        print(str(n)+' + ',end='')
    print(str(numinput[-1])+' = %s' % sum(numinput))
while True:
    number_input = input("Please enter an integer, or enter 0 to finish: ")
    if number_input == '0':
        results(numlist)
        break
    elif number_input not in allowed:
        try:
            digital(number_input)
        except ValueError as err:
            print(err)
            break
    else:
        numlist.append(int(number_input))
