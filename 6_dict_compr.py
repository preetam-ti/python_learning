keys = ['one', 'two', 'three']
values = [1, 2, 3]
key_value = {k: v for k,v in zip(keys, values)}

"""
#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)
"""
"""
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)
"""
"""
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)
"""

"""
Nested Dictionary with Two Dictionary Comprehensions
dictionary = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
print(dictionary)

Output:
{2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}, 
3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15},
4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20}}

"""