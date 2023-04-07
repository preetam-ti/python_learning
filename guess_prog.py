def double(x):
    return x * 2


sequence = [1, 3, 5, 9]

"""
doubled = [
    double(x) for x in sequence
]  # Put the result of double(x) in a new list, for each of the values in `sequence`

print(doubled)

doubled = map(double, sequence)
print(list(doubled))

#print(doubled)
"""
# -- Written as a lambda --

sequence = [1, 3, 5, 9]

doubled = map(lambda x: x * 2, sequence)
print(list(doubled))
