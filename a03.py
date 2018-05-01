'''
This is a program by Jerome Comeau
It calculates the BMI of the user from values input by the user.
Date Created: 04/25/2018
'''
import math 
print('Hi, and thanks for using my BMI Calculator.')
print('So let us start with some information.')
feet = int(input('Please tell me how tall you are in feet...  '))
inches = int(input('and in inches, please...  '))
pounds = int(input('and (please forgive the rudeness) your weight in pounds? '))

#now we do some math
#first we convert the hight into inches
total_inches = inches + (feet * 12)
inches_squared = total_inches * total_inches
weight_value = pounds * 703
BMI = weight_value / inches_squared

print('So, your height is {0} inches and your weight is {1} lbs, so your BMI is {2}'.format(total_inches, pounds, BMI))

