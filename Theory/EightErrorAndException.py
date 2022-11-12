#https://docs.python.org/3/tutorial/errors.html
print('#' * 50)
print('8. Errors and Exceptions')
print('-' * 50)
print('8.3. Handling Exceptions')
print('8.3.0.1 ', '.' * 50)

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

print('8.3.0.4 ', '.' * 50)
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)

print('8.3.0.5 ', '.' * 50)
import sys
try:
    f = open('workfile')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise



print('8.3.0.6 ', '.' * 50)
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


print('8.3.0.7 ', '.' * 50)
def this_fails():
    x = 1/0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)



print('-' * 50)
print('8.4. Raising Exceptions')
print('8.4.0.3 ', '.' * 50)

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise


print('-' * 50)
print('8.5. Exception Chaining')
print('8.5.0.1 ', '.' * 50)

# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")


print('-' * 50)
print('8.6. User-defined Exceptions')

print('-' * 50)
print('8.7. Defining Clean-up Actions')
print('8.7.0.1 ', '.' * 50)
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')


print('8.7.0.2 ', '.' * 50)

def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())


print('8.7.0.3 ', '.' * 50)
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

print(divide(2, 1))

print(divide(2, 0))

# print(divide("2", "1"))

print('-' * 50)
print('8.8. Predefined Clean-up Actions')
print('8.8.0.1 ', '.' * 50)

for line in open("workfile"):
    print(line, end="")

print('8.8.0.2 ', '.' * 50)

with open("workfile") as f:
    for line in f:
        print(line, end="")
