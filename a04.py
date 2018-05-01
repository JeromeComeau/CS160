'''
This is a program by Jerome Comeau
It allows the user to do some math, and checks to make sure the inputs are correct.
Date Created: 04/30/2018
'''
#import modules
import math
import operator

#define default values
oper = str('^')
first_num = 0
second_num = 0
#define allowable operators
allowed = ['+','-','*','/']
#insure operand input correctly, or ask until it is
while oper not in allowed:
    oper = input("Enter an operand (+,-,*,/) please: ")
else:
    #insure the values are recieved as integers
    first_num = int(input("Enter a number, please: "))
    second_num = int(input("Enter a second number, please: "))
    if second_num == 0 and oper == '/':
        #divide by zero error
        print("Sorry, cannot divide by zero!")
    else:
        #operator definitions because operand characters are tricky
        ops = {"+": operator.add,
               "-": operator.sub,
               "*": operator.mul,
               "/": operator.truediv}
        op_char = oper
        op_func = ops[op_char]
        result = op_func(first_num, second_num)
        #print the results in a decent format
        print("for {0} {1} {2} the result is {3}".format(first_num, oper, second_num, result))
