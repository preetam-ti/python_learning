
# -- Difference between two sets --

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# local_friends = ...
# If there are 3 friends, and 2 are abroad, that means that 1 friend is local.
# We can easily calculate which names are in `friends` but not in `abroad` by using `.difference`

local = friends.difference(abroad)
print(f'Difference is {local}')

print(f'Difference is {abroad.difference(friends)}')  # This returns an empty set

# -- Union of two sets --

local = {"Rolf"}
abroad = {"Bob", "Anne"}

# friends = ...
# If we have 1 local friend and 2 abroad friends, we could calculate the total friends by using `.union`

friends = local.union(abroad)
print(f'Union is {friends}')

# -- Intersection of two sets --

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

# Given these two sets of students, we can calculate those who do both art and science by using `.intersection`

both = art.intersection(science)
print(f'Intersection is {both}')


##Frozenset :

#Freeze the list, and make it unchangeable.we can do on tuple as well:

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)

# below line will generate error
x[1] = "strawberry"
#Exceptions while using Python frozenset() method
#If by mistake we want to change the frozenset object, then it throws a TypeError

# creating a dictionary
Student = {"name": "Ankit", "age": 21, "sex": "Male",
           "college": "MNNIT Allahabad", "address": "Allahabad"}
 
# making keys of dictionary as frozenset
key = frozenset(Student)
 
# printing dict keys as frozenset
print('The frozen set is:', key)