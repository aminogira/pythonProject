# https://docs.python.org/3.11/tutorial/datastructures.html#using-lists-as-stacks

print('#' * 50)
print('5.2. The del statement')

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print('A del a[0]  ', '.' * 5, a)

del a[2:4]
print('A del a[2:4]  ', '.' * 5, a)

del a[:]
print('A del a[:]  ', '.' * 5, a)

del a
# print(a)

print('#' * 50)
print('5.3. Tuples and Sequences')

t = 12345, 54321, 'hello!'

print('t  ', '.' * 5, t)
print('t[0]  ', '.' * 5, t[0])

u = t, (1, 2, 3, 4, 5)
print('u ', '.' * 5, u)
# Tuples are immutable: cannot assing new values
# t[0] = 88888

v = ([1, 2, 3], [3, 2, 1])
print('v ', '.' * 5, v)

empty = ()
print('empty', '.' * 5, empty)
print('len(empty)', '.' * 5, len(empty))

singleton = 'hello',
print('singleton', '.' * 5, singleton)
print('len(singleton)', '.' * 5, len(singleton))

print('#' * 50)
print('5.4. Sets')

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange in basket ', '.' * 5, 'orange' in basket)
print('crabgrass in basket ', '.' * 5, 'crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print('a ', '.' * 5, a) # unique letters in a
print('b ', '.' * 5, b)

print('a - b ', '.' * 5, a - b) # letters in a but not in b
print('a | b ', '.' * 5, a | b) # letters in a or b or both
print('a & b ', '.' * 5, a & b) # letters in a or b or both
print('a ^ b ', '.' * 5, a ^ b) # letters in a or b but not both

q = {x for x in 'abracadabra' if x not in 'abc'}
print('q ', '.' * 5, q)



print('#' * 50)
print('5.5. Dictionaries¶')

tel = {'jack': 4098, 'sape': 4139}
print('tel ', '.' * 5, tel)
tel['guido'] = 4127
print('tel ', '.' * 5, tel)
print('tel[jack] ', '.' * 5, tel['jack'])
del tel['sape']
print('tel ', '.' * 5, tel)
tel['irv'] = 4127
print('tel ', '.' * 5, tel)
print('list(tel) ', '.' * 5, list(tel))
print('sorted(tel)', '.' * 5, sorted(tel))

print('guido in tel', '.' * 5, 'guido' in tel)
print('jack not in tel', '.' * 5, 'jack' not in tel)

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print({x: x**2 for x in (2, 4, 6)})

print(dict(sape=4139, guido=4127, jack=4098))


print('#' * 50)
print('5.6. Looping Techniques')

print('A', '.' * 5, 'dictionaries')
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

print('B', '.' * 5, 'enumerate')
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

print('C', '.' * 5, 'zip')
questions = ['name', 'quest', 'favorite color']
answers = ['amila', 'the holy grail', 'white']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

print('D', '.' * 5, 'reversed')
for i in reversed(range(1, 10, 2)):
    print(i)
print('E', '.' * 5, 'sorted')
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

print('F', '.' * 5, 'sorted set')
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

print('G', '.' * 5, 'simpler and safer to create a new list ')
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
print('G-1', '.' * 5, raw_data)
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print('G-2', '.' * 5, filtered_data)


print('#' * 50)
print('5.7. More on Conditions')

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3

print('non_null', '.' * 5, non_null)