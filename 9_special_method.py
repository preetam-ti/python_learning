class Employee:
    raise_amount = 1.04
    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() +"."+ last.lower() +"@company.com"

    def fullname(self):
        #return 'Fullname is {} {}'.format(self.first, self.last)
        return f'Fullname is {self.first} {self.last}'
    
    def aply_raise(self):
        self.pay = int(self.pay*int(self.raise_amount))

    #repr is meant to be unambiguos representation of the object and should be used for 
    # debugging and logging and things like that it's really meant to be seen by other developers
    def __repr__(self) -> str:
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    #str is meant to be more of a readable representation of an object and is meant to be 
    # used as a display to the end user
    def __str__(self) -> str:
        return '{} - {}'.format(self.fullname(), self.email)

    #custom add megic method
    def __add__(self, other):
        return self.pay + other.pay
    


emp1 = Employee('Preetam', 'Singh', 1000000)
emp2 = Employee('test', 'user', 10000)

print(emp1)
print(repr(emp1))
print(str(emp2))

print(emp1.__repr__())
print(emp1.__str__())

"""
print(1+2)
#actaully calling below special method:
print(int.__add__(1,2))
print(str.__add__('a', 'b'))
"""

#when we call emp1+emp2 it will actually call __add__ method above.
print(emp1+emp2)

#__len__ special method
print(len('test'))
print('test'.__len__())

##https://docs.python.org/3/reference/datamodel.html#special-method-names

