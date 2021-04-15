'''
Given a three-digit number. Find the sum of its digits.
'''
x=int(input("enter any three digit number: "))
a= 0
while x>0:
    b=x%10
    a=a+b
    x=x//10
print(a)

