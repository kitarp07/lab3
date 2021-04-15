'''
given three integers, print the samallest one
'''

num1= int(input("enter any number: "))
num2= int(input("enter any number: "))
num3= int(input("enter any number: "))
if num1>num2 and num3>num2:
    print(f'{num2} is the smallest number')
elif num2>num3 and num1>num3:
    print(f'{num} is the smallest number')
elif num3>num1 and num2>num1:
    print(f'{num1} is the smallest number')