# Implicit type Casting
 
# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts
# c to float as it is a float addition
c = a + b
print(c)
print(type(c))
 
# Python automatically converts
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))

#Explicit Type Casting

#Type Casting int to float:
#Here, we are casting integer object to float object with float() function.
# int variable
a = 5
 
# typecast to float
n = float(a)
 
print(n)
print(type(n))

#Type Casting float to int:
# type Casting
 
# int variable
a = 5.9
 
# typecast to int
n = int(a)
 
print(n)
print(type(n))

# Type casting int to string:
 
# int variable
a = 5
 
# typecast to str
n = str(a)
 
print(n)
print(type(n))

##
"""
# input age
age = int(input("Enter Age : "))

# condition to check voting eligibility
if age>=18:
        status="Eligible"
else:
    status="Not Eligible"

print("You are ",status," for Vote.")
"""