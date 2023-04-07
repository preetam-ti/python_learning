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
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    #If you don't need access to the attributes or methods of the class or instance,
    #a staticmethod is better than a classmethod or instancemethod .
    #Static methods are used when we don't want subclasses of a class change/override a specific
    #implementation of a method.15
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True


#test1
emp1 = Employee('Preetam', 'Singh', 1000000)
emp2 = Employee('test', 'user', 10000)
emp1.raise_amount = 1.05
#print(emp1.fullname())
print(emp1.__dict__)


print(Employee.raise_amount) #calling class variable
print(emp1.raise_amount) #calling instance varible
print(emp2.raise_amount)#calling class variable
#

#CLASS METHOD:
#change class variable value using class method.
Employee.set_raise_amt(1.05)

#emp1.set_raise_amt(1.05) #we can also call class method usig object
print(Employee.raise_amount) #calling class variable
print(emp1.raise_amount)

#FROM_STRING CLASS METHOD
emp_str_1 = 'Preetam-Singh-70000'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)
new_emp_1.aply_raise()
print(new_emp_1.pay)

##regular method pass the first argument instance as a self and class method take first argument 
# class as a cls and static method dont pass anything automatically

#STATIC METHOD:
import datetime
my_date = datetime.date(2022, 2, 2)
print(Employee.is_workday(my_date))



