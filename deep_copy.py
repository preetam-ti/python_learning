import copy
x = [5,6,9,10]
y = x

print(y)
print(f'xid is {id(x)} and yid {id(y)}')
y[1] = 2
x[2] = 14
print(f'x is {x} and y is {y}')

z = copy.deepcopy(x)
print(z)
print(f'xid is {id(x)} and zid {id(z)}')
z[1] = 20
x[2] =25
print(f'x is {x} and z is {z}')