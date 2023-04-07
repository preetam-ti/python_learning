class Employee:
 
    def __init__(self, name, dept, age):
        self.name = name
        self.dept = dept
        self.age = age
 
    def __repr__(self):
        return '{' + self.name + ', ' + self.dept + ', ' + str(self.age) + '}'
 
if __name__ == '__main__':
 
    employees = [
        Employee('John', 'IT', 28),
        Employee('Sam', 'Banking', 20),
        Employee('Joe', 'Finance', 25)
    ]
 
    # sort list by `name` in the natural order
    employees.sort(key=lambda x: x.name)
 
    # output: [{Joe, Finance, 25}, {John, IT, 28}, {Sam, Banking, 20}]
    print(employees)
 
    # sort list by `name` in reverse order
    employees.sort(key=lambda x: x.name, reverse=True)
 
    # output: [{Sam, Banking, 20}, {John, IT, 28}, {Joe, Finance, 25}]
    print(employees)



"""
#We can also use the operator.attrgetter() function to produce value for the key attribute. 
# It returns a callable object that fetches a specified attribute from its operand.

from operator import attrgetter
 
class Employee:
 
    def __init__(self, name, dept, age):
        self.name = name
        self.dept = dept
        self.age = age
 
    def __repr__(self):
        return '{' + self.name + ', ' + self.dept + ', ' + str(self.age) + '}'
 
if __name__ == '__main__':
 
    employees = [
        Employee('John', 'IT', 28),
        Employee('Sam', 'Banking', 20),
        Employee('Joe', 'Finance', 25)
    ]
 
    employees.sort(key=attrgetter('name'))
 
    # output: [{Joe, Finance, 25}, {John, IT, 28}, {Sam, Banking, 20}]
    print(employees)
    
    
    
    
    """

    """
    
    # explicit function sort names
# by their surnames
def sortSur(nameList):
    l2 = []
 
    # create 2d list of names
    for ele in nameList:
        l2.append(ele.split())
    nameList = []
 
    # sort by last name
    for ele in sorted(l2, key=lambda x: x[-1]):
        nameList.append(' '.join(ele))
 
    # return sorted list
    return nameList
 
 
# Driver Code
 
# assign list of names
nameList = ['John Wick', 'Jason Voorhees',
            'Freddy Krueger', 'Keyser Soze',
            'Mohinder Singh Pandher']
 
# display original list
print('\nList of Names:\n', nameList)
print('\nAfter sorting:\n', sortSur(nameList))

#OR
def sortSur(nameList):
     
    # sort list by last name
    nameList.sort(key=lambda x: x.split()[-1])
     
    # return sorted list
    return nameList


    """