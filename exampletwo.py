def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

print("\n==================================")
# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
def ff(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(ff(1))
print(ff(2))
print(ff(3))


print("\n==================================")
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)                                          # 1 positional argument
print("\n------------------")
parrot(voltage=1000)                                  # 1 keyword argument
print("\n------------------")
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
print("\n------------------")
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
print("\n------------------")
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
print("\n------------------")
parrot('a thousand', state='pushing up the daisies')

print("\n==================================")
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
            "It's really very, VERY runny, sir.",
            shopkeeper="Michael Palin",
            client="John Cleese",
            sketch="Cheese Shop Sketch")

print("\n==================================")
print("\n==================================")
print("\n==================================")
print("\n==================================")


https://docs.python.org/3.11/tutorial/controlflow.html