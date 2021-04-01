'''
if  name is less than 3 character long - name must be at least 3 characters
otherwise if it's more
than 50 characters - name must be maximum of 50 characters
other wise - name looks good
'''

name=input("enter the name :  ")
if len(name)< 3:
    print('name must be at least 3 characters')
elif len(name)> 50:
    print("name musts be a maximum of 50 characters")
else:
    print('name looks good')

la=len(name)
print (la)