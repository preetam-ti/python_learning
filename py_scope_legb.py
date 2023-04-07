#Example 1: Scope and Namespace in Python

# global_var is in the global namespace
global_var = 10

def outer_function():
    #  outer_var is in the local namespace 
    outer_var = 20

    def inner_function():
        #  inner_var is in the nested local namespace 
        inner_var = 30

        print(inner_var)

    print(outer_var)

    inner_function()

# print the value of the global variable
print(global_var)

# call the outer function and print local and nested local variables
outer_function()

#Output : 10 20 30

#Here,

#global_var - is in the global namespace with value 10
#outer_val - is in the local namespace of outer_function() with value 20
#inner_val - is in the nested local namespace of inner_function() with value 30

####
#Example 2: Use of global Keyword in Python

# define global variable 
global_var = 10

def my_function():
    # define local variable
    local_var = 20

    # modify global variable value 
    global global_var
    global_var = 30

# print global variable value
print(global_var)

# call the function and modify the global variable
my_function()

# print the modified value of the global variable
print(global_var)

##
#Nested Functions: The Enclosing Scope : Enclosing or nonlocal scope is observed when you nest functions inside other functions.
#nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.

# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()

#With the statement nonlocal var, you tell Python that you’ll be modifying var inside nested().
#output 
#inner: nonlocal
#outer: nonlocal