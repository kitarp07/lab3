'''
For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.
'''
x= int(input("enter any number: "))
if x>0:
    print(f'{x} is positive')
elif x<0:
    print(f'{x}  is negative')
else:
    print("zero")