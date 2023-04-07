#Program of String formatting in Python

#Method 1: Formatting string using % Operator
name = 'Jay'
print('Hello %s' % name)

#multiple string using % Operator
print("%s is learning %s "%(name,"Python"))

print('There are %d dogs.' %4)

#Method 2: Using format() method

print('We all are {}.'.format('equal'))

#We can insert string by using index-based position:
print('{2} {1} {0}'.format('directions','the', 'Read'))

#Using assigned keywords:
print('a: {a}, b: {b}, c: {c}'.format(a = 1,c = 12.3, b = 'Two'))

#Method 3: Formatted String using F-strings
name = 'Ele'
 
print(f"My name is {name}.")

#Arithmetic operations using F-strings
a = 5
b = 10
 
print(f"He said his age is {2 * (a + b)}.")

#Lambda Expressions using F-strings
print(f"He said his age is {(lambda x: x*2)(3)}")

#Method 4: String Template Class