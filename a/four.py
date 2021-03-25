'''
wap which accepts marks of four subjects and display total marks, percentage and grade
'''

sub1=float(input('enter the marks of 1st subject: '))
sub2=float(input('enter the marks of 2nd subject: '))
sub3=float(input('enter the marks of 3rd subject: '))
sub4=float(input('enter the marks of 4th subject: '))
totalmarks = sub1+sub2+sub3+sub4
fullmarks= 400
print(f'the total marks is{totalmarks}')
percentage= (totalmarks/fullmarks)*100
print(f'the percentage is {percentage}')
if percentage>=70:
    print('distinction')
if percentage>60 and percentage<70:
    print('first division')
if percentage>40 and percentage<60:
    print('pass')
if percentage<40:
    print('fail')
