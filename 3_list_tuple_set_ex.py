l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

# Access individual items in lists and tuples using the index.
print(l[0])
print(t[0])
# print(s[0])  # This gives an error because sets are unordered, so accessing element 0 of something without order doesn't make sense.

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
