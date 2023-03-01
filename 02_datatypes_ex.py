#NUMERIC DATA TYPES:
#create a variable with integer value.
a=100
#create a variable with float value.
b=10.2345
#create a variable with complex value.
c=100+3j
print(f'type of a is {type(a)}, type of b is {type(b)} and type of c is {type(c)}')

print(f'sum of a and b is {a+b}')

#Complex ex
#When both the parameters are provided to the complex() method:
#complex is useful in electronics calculation
real = 10
imaginary = 7
complex_number = complex(real, imaginary)
print("Complex number formed: ", complex_number)
#Output : Complex number formed:  (10+7j)

#STRING DATA TYPE:
a = "string in a double quote"
b= 'string in a single quote'
print(a)
print(b)

# using ',' to concatenate the two or several strings
print(a,"concatenated with",b)

#using '+' to concate the two or several strings
print(a+" concated with "+b)

# characters of String 
String1 = "teamtraining"
print("Initial String: ") 
print(String1) 
    
# Printing First character 
print("\nFirst character of String is: ") 
print(String1[0]) 
    
# Printing Last character 
print("\nLast character of String is: ") 
print(String1[-1])

#BOOLEAN DATATYPE:
a_true_alias = True
print(a_true_alias)
print(type(a_true_alias))
#True = 5
#output :   File "<stdin>", line 1
#SyntaxError: cannot assign to True

print(5 == 5)  # True
print(5 > 5)  # False
print(10 != 10)  # False

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)  # True
print(friends is abroad)  # False

###
# int to bytes
str = "Welcome to Python Learning"
 
arr = bytes(str, 'utf-8')
 
print(arr)