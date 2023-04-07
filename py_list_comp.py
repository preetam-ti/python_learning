#https://www.geeksforgeeks.org/python-list-comprehension/
"""
    List comprehensions are used for creating new lists from other iterables like tuples, 
    strings, arrays, lists, etc. A list comprehension consists of brackets containing the 
    expression, which is executed for each element along with the for loop to iterate over each element. 
    newList = [ expression(element) for element in oldList if condition ] 
    Advantages of List Comprehension
        1.More time-efficient and space-efficient than loops.
        Require fewer lines of code.
        Transforms iterative statement into a formula.

"""

# Import required module
import time
 
 
# define function to implement for loop
def for_loop(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result
 
 
# define function to implement list comprehension
def list_comprehension(n):
    return [i**2 for i in range(n)]
 
 
# Driver Code 
 
# Calculate time takens by for_loop()
begin = time.time()
for_loop(10**6)
end = time.time()
 
# Display time taken by for_loop()
print('Time taken for_loop:',round(end-begin,2))
 
# Calculate time takens by list_comprehension()
begin = time.time()
list_comprehension(10**6)
end = time.time()
 
# Display time taken by for_loop()
print('Time taken for list_comprehension:',round(end-begin,2))

"""List = [character for character in 'Geeks 4 Geeks!']
 
# Displaying list
print(List)
"""

"""matrix = []
 
for i in range(3):
     
    # Append an empty sublist inside the list
    matrix.append([])
     
    for j in range(5):
        matrix[i].append(j)
         
print(matrix)"""


"""# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
 
print(matrix)
"""

"""
# using lambda to print table of 10
numbers = list(map(lambda i: i*10, [i for i in range(1,6)]))
 
print(numbers)
"""

"""# Getting square of even numbers from 1 to 10
squares = [n**2 for n in range(1, 11) if n%2==0]
 
# Display square of even numbers
print(squares)"""

"""# Initializing string
string = 'Geeks4Geeks'
 
# Toggle case of each character
List = list(map(lambda i: chr(ord(i)^32), string))
 
# Display list
print(List)"""

"""
# Reverse each string in tuple
List = [string[::-1] for string in ('Geeks', 'for', 'Geeks')]
 
# Display list
print(List)
"""


##
numbers = [1, 3, 5]
squares = [x * 2 for x in numbers]

# -- Dealing with strings --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)


# -- Can make a new list of friends whose name starts with S --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)

# -- List comprehension creates a _new_ list --

friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]  # same as above

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), " starts_s: ", id(starts_s))
