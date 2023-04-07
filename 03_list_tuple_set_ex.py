l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

# Access individual items in lists and tuples using the index.
print(l[0])
print(t[0])
# print(s[0]) # This gives an error because sets are unordered, so accessing element 0 of something without order doesn't make sense.

# Modify individual items in lists using the index.
l[0] = "Smith"
# t[0] = "Smith"  # This gives an error because tuples are "immutable".

print(l)
print(t)

# Add to a list by using `.append`
l.append("Jen")
print(l)
# Tuples cannot be appended to because they are immutable.

# Add to sets by using `.add`
s.add("Jen")
print(s)

# Sets can't have the same element twice.
s.add("Bob")
print(s)

##########
#del
list_a = [1, 2, 3, 4]
del(list_a[0])
print(list_a)
#[2, 3, 4]

#remove
list_a = ['a','b',3,6]
list_a.remove('a')
print(list_a)
#['b', 3, 6]
set_a = {'a','b',3,6}
set_a.remove('a')
print(set_a)
#{3, 6, 'b'}

#pop in list:
list_a = ['a','b',3,6,4]
item = list_a.pop()
print(list_a)
#['a', 'b', 3, 6]
print(item)
#4

######
a = [1,2,3,'a',1,3,5]
print(tuple(a))
#(1, 2, 3, 'a', 1, 3, 5)
print(set(a))
#{1, 2, 3, 5, 'a'}


###
# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get the last value
print(fruits[-1])



# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop using index
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list   :Python uses an algorithm called Timsort: Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)

# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print(fruits[1])

# Can't change value
fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)

###
tuple_A = ('Name = John Cleverly','Grade = Grade 2','ID = 123', 'Section = B')
list_B  = ['Milk','Butter', 'Dessert', 'Ice cream']


print('size of a tuple is : ',tuple_A.__sizeof__())
print('size of a list is : ',list_B.__sizeof__())
#OUTPUT:
    #size of a tuple is :  56
    #size of a list is :  72

##iteration over list vs iteration over tuple:

import sys, platform
import time
 
l=list(range(100000001))
t=tuple(range(100000001))
 
start = time.time_ns()
for i in range(len(t)):
    a = t[i]
end = time.time_ns()
print("Total lookup time for Tuple: ", end - start)
 
start = time.time_ns()
for i in range(len(l)):
    a = l[i]
end = time.time_ns()
print("Total lookup time for LIST: ", end - start)

####Output:
#Total lookup time for Tuple:  7038208700
#Total lookup time for LIST:  19646516700