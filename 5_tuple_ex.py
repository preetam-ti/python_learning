# Tuple unpacking
Tuple1 = ("Geeks", "For", "Geeks")
 
# This line unpack
# values of Tuple1
a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)

# Concatenation of tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')
 
Tuple3 = Tuple1 + Tuple2

##Slicing
# Tuple1 = tuple('GEEKSFORGEEKS')
 
# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])
 
# Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])
 
# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])


# Deleting a Tuple
del Tuple1
