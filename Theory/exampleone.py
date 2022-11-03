words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

print("\n==================================")
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
    print(user)

print("\n==================================")
# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
    print(user)

print("\n==================================")
for i in range(5):
    print(i)


list(range(5, 10))

list(range(0, 10, 3))

list(range(-10, -100, -30))

print("\n==================================")
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print("\n== sum(range(4)) = 0 + 1 + 2 + 3")
print(sum(range(4)))



print("\n==================================")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

print("\n==================================")
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)


"""
print("\n==================================")
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

http_error(400)
"""
print("\n==================================")
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

print("\n==================================")
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result


f100 = fib2(100)
print(f100)

print("\n==================================")

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')
print("\n-------------")
ask_ok('OK to overwrite the file?', 2)
print("\n-------------")
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

print("\n==================================")
print("\n==================================")
print("\n==================================")
print("\n==================================")
print("\n==================================")
print("\n==================================")


