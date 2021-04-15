'''
Given a positive real number, print its fractional part.
'''
import math
num= float(input("enter any number: "))
fractionalpart= math.modf(num)
print(f'the fractional part of {num} is {fractionalpart}')

num= float(input("enter any number: "))
a=int(num)
fractionalpart= num-a
print(f'the fractional part of {num} is {fractionalpart}')


