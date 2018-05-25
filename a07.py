'''
This is a program by Jerome Comeau
Ths allows the user to input a binary string and returns the appropriate
decimal value.
Date Created: 05/24/2018
'''

def binset(binstr):
    if set(binstr) != {'0', '1'}:
#check to make sure the string only contains 0s and 1s
        raise ValueError('String is not binary: "%s"' % binstr)

def binlen(binstr):
#making sure that the string is 8 bits
    if len(binstr) != 8:
        raise ValueError('String is not 8-bit: "%s"' % binstr)

def bincalc(binstr):
    decimal = int(binstr,2)
    return decimal

while True:
#input loop! allows the user to quit out.
        binary = input("Enter a line of binary, enter 'q' to quit: ")

        if binary.lower() == 'q':
            break

        try:
            binlen(binary)
        except ValueError as err:
            print(err)
            break

        try:
            binset(binary)
        except ValueError as err:
            print(err)
            break

        try:
            print(bincalc(binary))
        except ValueError as err:
            print(err)
