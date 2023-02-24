
#
# Creating a Multi-Dimensional List
List = [['python', 'For'], ['devops']]
print(List[0][1])
print(List[1][0])

#Negative indexing
# print the last element of list
print(List[-1])
  
# print the third last element of list
print(List[-3])

#adding element
List.insert(0, 'devops')
#adding list:
List.extend([8, 'python', 'Always'])

# Reversing a list
mylist = [1, 2, 3, 4, 5, 'learn', 'Python']
mylist.reverse()
print(mylist)


# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6)


List.pop()
print("\nList after popping an element: ")
print(List)

#
List.pop(2)
print("\nList after popping a specific element: ")
print(List)

# Print elements of a range
# using Slice operation
Sliced_List = List[3:8]
# pre-defined point to end
Sliced_List = List[5:]
# beginning till end
Sliced_List = List[:]
# using negative index List slicing
Sliced_List = List[-6:-1]

# Printing elements in reverse
# using Slice operation
Sliced_List = List[::-1]

