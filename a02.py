import math
'''This program was written by Jerome Comeau.

For PCC Class CS-160-0-20629 

Date Created: 04/18/2018 '''

#input statement to read name from the user
name = input('Please enter your name:   ')
subject = input('Please enter your subject:   ')

#output text and variables
print('Hello ' + name + ', and welcome to my first Pyhton program.')
print('You will do well in ' + subject + ' if you work hard.')

#input for math problem, making sure that the input is an integer
#if the user inputs a string it will error out
#I'm sure there's a way to force it to ask again until it gets a number
#but I think that's beyond the scope of this exercise

first_number = int(input('Please enter a number:   '))
second_number = int(input('Please enter another number:   '))


#now let's do some math
the_sum = first_number + second_number
print('The sum of {0} and {1} = {2}'.format(first_number, second_number, the_sum))

the_difference = first_number - second_number
print('The difference of {0} and {1} = {2}'.format(first_number, second_number, the_difference))

the_product = first_number * second_number
print('The product of {0} and {1} = {2}'.format(first_number, second_number, the_product))

the_quotient = first_number / second_number
print('The quotient of {0} and {1} = {2}'.format(first_number, second_number, the_quotient))

the_remainder = first_number % second_number
print('The remainder of {0} and {1} = {2}'.format(first_number, second_number, the_remainder))

print('Thanks for using my program!')
