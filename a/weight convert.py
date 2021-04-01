'''
weight converter:
input the weight of a person in either kg or lbs. if the person provides his/ her weight in kg
then convert into lbs else convert it to kg
'''

weight= int(input("enter the weight of the person: "))
unit= input("enter the unit : ")
if unit == 'lbs':
    weight_in_kg= weight/2.205
    print(f'{weight} lbs is equal to {weight_in_kg} kg')
elif unit =='kg':
    weight_in_lbs = weight*2.205
    print(f'{weight} kg is equal to {weight_in_lbs } lbs')
