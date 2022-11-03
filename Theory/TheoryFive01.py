
#https://docs.python.org/3.11/tutorial/datastructures.html#using-lists-as-stacks

print('-' * 50)
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print('Full List ::', fruits)
print('N apple ::', fruits.count('apple'))
print('N tangerine ::',fruits.count('tangerine'))
print('Index banana ::', fruits.index('banana'))
print('Index banana after 4 ::', fruits.index('banana', 4))
print('Full List ::', fruits)
print('.' * 5 , 'reversing')
fruits.reverse()
print('Reverse list ::', fruits)
print('.' * 5 , 'appending grape')
fruits.append('grape')
print('Full List ::', fruits)
print('.' * 5 , 'sorting')
fruits.sort()
print('Full List ::', fruits)
print('.' * 5 , 'pop')
fruits.pop()
print('Full List ::', fruits)


print('#' * 50)
print('5.1.1. Using Lists as Stacks')
stack = [3, 4, 5]
print('full stack ', stack)
print('.' * 5, 'append')
stack.append(6)
stack.append(7)
print('full stack ', stack)
print('pop ...' , stack.pop())
print('full stack ', stack)
print('pop ...' , stack.pop())
print('pop ...' , stack.pop())
print('full stack ', stack)


print('#' * 50)
print('5.1.2. Using Lists as Queues')
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print('full Q :: ',queue)
print('append :: ',queue.append("Terry"))
print('append :: ',queue.append("Graham"))
print('full Q :: ',queue)
print('popleft :: ', queue.popleft())
print('popleft :: ', queue.popleft())
print('full Q :: ',queue)




print('#' * 50)
print('5.1.3. List Comprehensions')
squares = []
for x in range(10):
    squares.append(x**2)
print('.' * 5, 'sq 1')
print(squares)
print('.' * 5, 'sq 2')
squ2 =list(map(lambda x: x**2, range(10)))
print(squ2)
print('.' * 5, 'sq 3')
squ3 = [x**2 for x in range(10)]
print(squ3)

print('$' * 5, 'wow Aus!!!')
print ([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
print('$' * 5, 'equals to')
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print('.' * 5, combs)

print('#' * 50)
print('')
vec = [-4, -2, 0, 2, 4]
print( '.' * 5, vec)
# create a new list with the values doubled
print('Double List', '.' * 5, [x*2 for x in vec])
# filter the list to exclude negative numbers
print('exclued negative List', '.' * 5, [x for x in vec if x >= 0])
# apply a function to all the elements
print('function to all', '.' * 5, [abs(x) for x in vec])
# call a method on each element

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print('.' * 5, freshfruit)
# call a method on each element
print('function to all', '.' * 5, [weapon.strip() for weapon in freshfruit])
# create a list of 2-tuples like (number, square)
print('2-tuples ', '.' * 5, [(x, x**2) for x in range(6)])
# the tuple must be parenthesized, otherwise an error is raised
#print('tuple must be parenthesized ', '.' * 5, [x, x**2 for x in range(6)])

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print('.' * 5, vec)
print('listcomp with two for ', '.' * 5, [num for elem in vec for num in elem])


from math import pi
print('.' * 5, [str(round(pi, i)) for i in range(1, 6)])


print('.' * 5, '3x4 matrix implemented as a list of 3 lists of length 4')
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print( 'A ', '.' * 5, [[row[i] for row in matrix] for i in range(4)])
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print('B ','.' * 5, transposed)


trans = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    trans.append(transposed_row)
print('C ','.' * 5, trans)

print('D ','.' * 5, list(zip(*matrix)))


