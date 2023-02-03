# Take input from user

num = float(input('Enter a number: '))

'''
Use the user to input
to calculate the square root of the number
'''

# num & num_sqrt are literals ..... (Literals are the constants values assigned to the constant variables)

num_sqrt = num ** 0.5

print("The square root of %0.3f is %0.3f"%(num, num_sqrt))

# Indentation

if (num_sqrt <= 1):
    print("Foo")
else:
    print("Bar")    


