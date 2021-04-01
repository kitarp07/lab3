'''
price of a house is $1 million. if buyer has good credit, they need to put down 10% otherwise
they need to put down 20%
'''

credit = input("does buyer has a good credit? ")
if credit=="yes":
    payment= (10/100)*1000000
else:
    payment= (20/100)*1000000
print(payment)