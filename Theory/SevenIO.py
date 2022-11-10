#https://docs.python.org/3/tutorial/inputoutput.html
print('#' * 50)
print('7. Input and Output')
print('-' * 50)
print('7.1. Fancier Output Formatting')
print('7.1.0.1 ', '.' * 50)
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
print('7.1.0.2 ', '.' * 50)
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
print('7.1.0.3 ', '.' * 50)
s = 'Hello, world.'
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))

print('-' * 50)
print('7.1.1. Formatted String Literals')
print('7.1.1.1 ', '.' * 50)
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

print('7.1.1.2 ', '.' * 50)
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

print('7.1.1.3 ', '.' * 50)
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')

print('7.1.1.4 ', '.' * 50)
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')


print('-' * 50)
print('7.1.2. The String format() Method')
print('7.1.2.1 ', '.' * 50)
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('7.1.2.2 ', '.' * 50)
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

print('7.1.2.3 ', '.' * 50)
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print('7.1.2.4 ', '.' * 50)
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
print('7.1.2.5 ', '.' * 50)
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))



print('7.1.2.6 ', '.' * 50)
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

print('7.1.2.7 ', '.' * 50)
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('-' * 50)
print('7.1.3. Manual String Formatting')
print('7.1.3.1 ', '.' * 50)
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

print('7.1.3.2 ', '.' * 50)
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

print('7.1.3.3 ', '.' * 50)

print('The value of pi is approximately %5.3f.' % math.pi)



print('-' * 50)
print('7.2. Reading and Writing Files')

#f = open('workfile', 'w', encoding="utf-8")
#this will create new file

with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

f = open('workfile', 'r', encoding="utf-8")

print('7.2.1.1 ', '.' * 50)
#f.read()
#'This is the entire file.\n'

print('7.2.1.2 ', '.' * 50)
print( 'aa ' , f.readline())
'This is the first line of the file.\n'
print('bb ' ,f.readline())
'Second line of the file\n'
print('7.2.1.3 ', '.' * 50)
for line in f:
    print('ff ', line, end='')


print('7.2.1.4 ', '.' * 50)
#print(f.write('This is a test\n'))

for line in f:
    print('gg ', line, end='')

print('7.2.1.5 ', '.' * 50)
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
#f.write(s)

for line in f:
    print('hh ', line, end='')

print('7.2.1.6 ', '.' * 50)

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')


for line in f:
    print('ii ', line, end='')

f.seek(5)
print(f.read(5))


print('-' * 50)
print('7.2.2. Saving structured data with json')
print('7.2.2.1 ', '.' * 50)

import json
x = [1, 'simple', 'list']
print(json.dumps(x))

print('7.2.2.2 ', '.' * 50)
json.dump(x, f)
x = json.load(f)
print(x)

