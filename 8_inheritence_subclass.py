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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first: str, last: str, pay: int, prog_lang: str):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay) #we can do like this instead of super
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first: str, last: str, pay: int, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
        
    


dev1 = Developer('Preetam', 'Singh', 1000000, 'Python')
dev2 = Developer('test', 'user', 10000, 'Java')

#print(help(Developer)) # it will show MRO order 
#below dev object is calling Employee attribute
print(dev1.pay)
dev1.aply_raise()
print(dev1.pay)

print(dev1.prog_lang)


##MANAGER CLASS OBJECT:
mgr1 = Manager('Vijay', 'Kumar', 9000, [dev1])
print(mgr1.email)

mgr1.add_emp(dev2)
mgr1.print_emps()
#print(mgr1.__dict__)
mgr1.remove_emp(dev1)
mgr1.print_emps()

#print(Manager.mro())
#IS_INSTANCE
#print(isinstance(mgr1, Manager))  #True
#print(isinstance(mgr1, Developer)) #False
#print(isinstance(mgr1, Employee)) #True

#IS SUBCLASS
#print(issubclass(Manager, Employee))