
# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Python'
age = 3.11

# Concatenate
print('Hello, Learning' + name + ' and version is ' + str(age))

# string Methods

s = 'helloworld'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# get length
print(len(s))

# replace
print(s.replace('world', 'everyone'))

# count
sub = 'h'
print(s.count(sub))

# starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# is all alphabetic
print(s.isalpha())

# is all numeric
print(s.isnumeric())

#########