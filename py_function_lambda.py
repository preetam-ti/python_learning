# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello(name='Sam'):
    print(f'Hello {name}')


# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2: num1 + num2

print(getSum(10, 3))

def hello():
    print("Hello!")


hello()

# -- Defining vs. calling --
# It's still all sequential!


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")


print("Welcome to the age in seconds program!")
user_age_in_seconds()

print("Goodbye!")

# -- Don't reuse names --


def print():
    print("Hello, world!")  # Error!


# -- Don't reuse names, it's generally confusing! --
friends = ["Rolf", "Bob"]


def add_friend():
    friend_name = input("Enter your friend name: ")
    friends = friends + [friend_name]  # Another way of adding to a list!


add_friend()
print(friends)  # Always ['Rolf', 'Bob']

# -- Can't call a function before defining it --

#say_hello()

def say_hello():
    print("Hello!")

# -- Remember function body only runs when the function is called --
def add_friend():
    friends.append("Rolf")


friends = []
add_friend()

print(friends)  # [Rolf]

##

def add(x, y):
    result = x + y
    print(result)


add(2, 3)  # 5

# -- If a function doesn't have parameter, you can't give it arguments --


def say_hello():
    print("Hello!")


say_hello("Bob")  # Error

# -- But if you add a parameter, then you must give it an argument --


def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Bob")
say_hello()  # Error, needs an argument

# -- Keyword arguments --
# To make things clearer, in Python you can give keyword arguments.


def say_hello(name):
    print(f"Hello, {name}!")


say_hello(name="Bob")  # Obvious that this is someone's name


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")


divide(dividend=15, divisor=3)
divide(15, 0)
divide(15, divisor=0)  # That's OK
# divide(dividend=15, 0)  # Not OK, named arguments must go after positional arguments

##default parameter:
def add(x, y=3):
    print(x + y)


add(5)  # 8
add(5, 8)  # 13
add(y=3)  # Error, missing x

# -- Order of default parameters --

# def add(x=5, y):  # Not OK, default parameters must go after non-default
#     print(x + y)




####
def add(x, y):
    return x + y


print(add(5, 7))

# -- Written as a lambda --

add = lambda x, y: x + y
print(add(5, 7))

# Four parts
# lambda
# parameters
# :
# return value

# Lambdas are meant to be short functions, often used without giving them a name.
# For example, in conjunction with built-in function map
# map applies the function to all values in the sequence


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]

doubled = [
    double(x) for x in sequence
]  # Put the result of double(x) in a new list, for each of the values in `sequence`
doubled = map(double, sequence)
print(list(doubled))

# -- Written as a lambda --

sequence = [1, 3, 5, 9]

doubled = map(lambda x: x * 2, sequence)
print(list(doubled))

# -- Important to remember --
# Lambdas are just functions without a name.
# They are used to return a value calculated from its parameters.
# Almost always single-line, so don't do anything complicated in them.
# Very often better to just define a function and give it a proper name.